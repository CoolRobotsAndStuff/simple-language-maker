#!/usr/bin/env python3

from collections import defaultdict
import sys
import random
import textwrap

from asciimatics.widgets import Frame, Layout, Divider, Button, TextBox, Widget, VerticalDivider, ListBox
from asciimatics.scene import Scene
from asciimatics.renderers import SpeechBubble
from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics import utilities
from asciimatics.strings import ColouredText

from src import internal
from src.cli.custom_widgets import WrappedTextBox, Title, WrappedTextBoxEffect
from src.cli.languages import spanish

from pathlib import Path

import tkinter

from tkinter import filedialog

my_palette = defaultdict(
        lambda: (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        {
            "invalid": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_RED),
            "label": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "title": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "selected_focus_field": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "focus_edit_text": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "focus_button": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "selected_focus_control": (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLACK),
            "disabled": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "scroll" : (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }
)

class TranslatorModel:
    def __init__(self) -> None:
        self.current_generated_language = internal.make_random_language()
        self.current_loaded_language = internal.SimpleLanguage("???", [])
        self.language_pack = spanish(self.current_generated_language, self.current_loaded_language)
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

    def set_random_language(self):
        self.current_generated_language = internal.make_random_language()
        self.language_pack = spanish(self.current_generated_language, self.current_loaded_language)

    def save_current_language(self):
        file_name = self.current_generated_language.name + internal.FILE_EXTENSION
        file_path = filedialog.asksaveasfilename(defaultextension=internal.FILE_EXTENSION, initialfile=file_name)
        try:
            if isinstance(file_path, str):
                internal.save_to_file(Path(file_path), self.current_generated_language)
        except IsADirectoryError:
            pass
    
    def open_language_from_file(self):
        file = filedialog.askopenfilename(defaultextension=internal.FILE_EXTENSION, filetypes=[("Simple Language files", f"*{internal.FILE_EXTENSION}")])
        try:
            if isinstance(file, str):
                self.current_loaded_language = internal.open_from_file(Path(file))
                self.language_pack = spanish(self.current_generated_language, self.current_loaded_language)
        except IsADirectoryError:
            pass

    def translate_file(self):
        input_file_name = filedialog.askopenfilename(defaultextension=".txt")
        try:
            if isinstance(input_file_name, str):
                input_file_name = Path(input_file_name)
                with open(input_file_name, "r") as input_file:
                    input_text = input_file.readlines()

                new_file_name, extension = input_file_name.name.split(".")

                new_file_name += f"_{self.language_pack['file']['translated_to']}_{self.current_loaded_language.name}.{extension}"

                fonetized = internal.fonetize("\n".join(input_text))
                translated = internal.translate(fonetized, self.current_loaded_language)
                output_file_name = filedialog.asksaveasfilename(defaultextension=extension, initialfile=new_file_name)
                if isinstance(output_file_name, str):
                    with open(output_file_name, "w") as output_file:
                        output_file.write(translated)
        except IsADirectoryError:
            pass

    def detranslate_file(self):
        try:
            input_file_name = filedialog.askopenfilename(defaultextension=".txt")
            if isinstance(input_file_name, str):
                input_file_name = Path(input_file_name)
                with open(input_file_name, "r") as input_file:
                    input_text = input_file.read()

                new_file_name, extension = input_file_name.name.split(".")

                new_file_name += f"_{self.language_pack['file']['translated_to']}_{self.language_pack['file']['nat_lang_name']}.{extension}"

                translated = internal.detranslate(input_text, self.current_loaded_language)
                output_file_name = filedialog.asksaveasfilename(defaultextension=extension, initialfile=new_file_name)
                if isinstance(output_file_name, str):
                    with open(output_file_name, "w") as output_file:
                        output_file.write(translated)
        except IsADirectoryError:
            pass

class TabButtons(Layout):
    def __init__(self, frame: Frame, active_tab_idx):
        cols = [1, 1, 1]
        super().__init__(cols)
        self._frame = frame
        btns = [Button("Inicio", self._on_click_1),
                Button("Nuevo", self._on_click_2),
                Button("Traducir", self._on_click_3),
                Button("Salir", self._on_click_Q)]
        del btns[active_tab_idx]
        for i, btn in enumerate(btns):
            self.add_widget(btn, i)

    def _on_click_1(self):
        raise NextScene("Tab1")

    def _on_click_2(self):
        raise NextScene("Tab2")

    def _on_click_3(self):
        raise NextScene("Tab3")
    
    def _on_click_Q(self):
        raise StopApplication("Salir")


class HomeUIFrame(Frame):
    def __init__(self, screen, language_pack, y):

        super().__init__(screen,
                         height=screen.height - y,
                         width=screen.width,
                         can_scroll=False, y=y)
        self.palette = my_palette
        layout0 = Layout([1], True)
        instructions = WrappedTextBox(Widget.FILL_FRAME, line_wrap=True, readonly=True)
        instructions.hide_cursor = True
        
        instructions.value = language_pack['home']['instructions']
        instructions.disabled = True
        
        self.add_layout(layout0)
        layout0.add_widget(instructions)
        
        
        layout1 = Layout([1])
        self.add_layout(layout1)
        layout1.add_widget(Divider())

        layout2 = TabButtons(self, 0)
        self.add_layout(layout2)
        self.fix()

class HomeScene(Scene):
    def __init__(self, screen, language_pack, clear=True, name=None):
        title = WrappedTextBoxEffect(screen, language_pack["home"]["title"], screen.width - 4)
        super().__init__([title, HomeUIFrame(screen, language_pack, y=title.height)], -1, clear, name)

class NewLanguageUIFrame(Frame):
    def __init__(self, screen: Screen, model: TranslatorModel, y):
        self._model = model

        super().__init__(screen,
                         height=screen.height - y,
                         width=screen.width,
                         can_scroll=False, y=y)
        self.palette = my_palette

        self.my_screen = screen


        title_layout = Layout([1])
        self.add_layout(title_layout)
        self.title_box = WrappedTextBox(1, line_wrap=True, readonly=True, justify='center')
        self.title_box.value = self._model.language_pack["new_language"]["title"]
        self.title_box.disabled = True


        instructions_box = WrappedTextBox(4, line_wrap=True, readonly=True, justify='left')
        instructions_box.value = self._model.language_pack["new_language"]["instructions"]
        instructions_box.disabled = True


        title_layout.add_widget(self.title_box)
        title_layout.add_widget(Divider())
        title_layout.add_widget(instructions_box)

        divider_layout15 = Layout([1])
        self.add_layout(divider_layout15)
        divider_layout15.add_widget(Divider())

        translator_layout = Layout([18, 1, 18], fill_frame=True)
        self.add_layout(translator_layout)
        self.translation_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True, readonly=True)
        translator_layout.add_widget(self.translation_text, 2)
        #self.translation_text.disabled = True
        self.translation_text.value = [""]

        translator_layout.add_widget(VerticalDivider(), 1)

        self.input_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True, on_change=self.on_text_edit)
        self.input_text.value = self._model.language_pack["new_language"]["test_poetry"]
        translator_layout.add_widget(self.input_text, 0)

        divider_layout2 = Layout([1])
        self.add_layout(divider_layout2)
        divider_layout2.add_widget(Divider())

        translator_buttons_layout = Layout([1, 1])
        self.add_layout(translator_buttons_layout)
        translator_buttons_layout.add_widget(Button(self._model.language_pack["new_language"]["new_button"][0], on_click=self.new_language), 0)
        translator_buttons_layout.add_widget(Button(self._model.language_pack["new_language"]["save_button"][0], on_click=self._model.save_current_language), 1)

        divider_layout3 = Layout([1])
        self.add_layout(divider_layout3)
        divider_layout3.add_widget(Divider())

        tab_buttons_layout = TabButtons(self, 1)
        self.add_layout(tab_buttons_layout)
        self.fix()

    def on_text_edit(self):
        fonetized = internal.fonetize("\n".join(self.input_text.value))
        self.translation_text.value = internal.translate(fonetized, self._model.current_generated_language).split("\n")

    def new_language(self):
        self._model.set_random_language()
        self.on_text_edit()
        self.title_box.value = self._model.language_pack["new_language"]["title"]


class NewLanguageScene(Scene):
    def __init__(self, screen, model, clear=True, name=None):
        super().__init__([NewLanguageUIFrame(screen, model, y=0)], -1, clear, name)


class TranslatorUIFrame(Frame):
    def __init__(self, screen: Screen, model: TranslatorModel, y):
        self._model = model

        super().__init__(screen,
                         height=screen.height - y,
                         width=screen.width,
                         can_scroll=False, y=y)
        self.palette = my_palette

        self.my_screen = screen


        self.palette = my_palette

        self.my_screen = screen


        title_layout = Layout([1])
        self.add_layout(title_layout)
        self.title_box = WrappedTextBox(1, line_wrap=True, readonly=True, justify='center')
        self.title_box.value = self._model.language_pack["translator"]["title"]
        self.title_box.disabled = True

        self.instructions_box = WrappedTextBox(6, line_wrap=True, readonly=True, justify='left')
        self.instructions_box.value = self._model.language_pack["translator"]["instructions"]
        self.instructions_box.disabled = True

        title_layout.add_widget(self.title_box)
        title_layout.add_widget(Divider())
        title_layout.add_widget(self.instructions_box)
        title_layout.add_widget(Divider())


        direction_chooser_layout = Layout([1, 2, 2, 1])
        self.add_layout(direction_chooser_layout)
        label = WrappedTextBox(3, line_wrap=True, readonly=True, justify='right')
        label.value = self._model.language_pack["translator"]["translation_direction"]
        label.disabled = True
        direction_chooser_layout.add_widget(label, 1)

        self.language_selector = ListBox(3, [(self._model.language_pack["translator"]["nat_lang_to_gen"], 1), \
                                             (self._model.language_pack["translator"]["gen_lang_to_nat"], 2)], \
                                              centre=True, on_change=self.on_text_edit)
        
        direction_chooser_layout.add_widget(self.language_selector, 2)

        divider_layout15 = Layout([1])
        self.add_layout(divider_layout15)
        divider_layout15.add_widget(Divider())

        translator_layout = Layout([18, 1, 18], fill_frame=True)
        self.add_layout(translator_layout)
        self.translation_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True, readonly=True)
        translator_layout.add_widget(self.translation_text, 2)
        #self.translation_text.disabled = True
        self.translation_text.value = [""]

        translator_layout.add_widget(VerticalDivider(), 1)

        self.input_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True, on_change=self.on_text_edit)
        self.input_text.value = self._model.language_pack["translator"]["text_hint"]
        translator_layout.add_widget(self.input_text, 0)

        divider_layout2 = Layout([1])
        self.add_layout(divider_layout2)
        divider_layout2.add_widget(Divider())

        translator_buttons_layout = Layout([1, 1])
        self.add_layout(translator_buttons_layout)
        translator_buttons_layout.add_widget(Button(self._model.language_pack["translator"]["load_lang_button"], on_click=self.open_language), 0)
        translator_buttons_layout.add_widget(Button(self._model.language_pack["translator"]["translate_file_button"], on_click=self.translate_file), 1)

        divider_layout3 = Layout([1])
        self.add_layout(divider_layout3)
        divider_layout3.add_widget(Divider())

        tab_buttons_layout = TabButtons(self, 2)
        self.add_layout(tab_buttons_layout)
        self.fix()

    def on_text_edit(self):
        if self.language_selector.value == 1:
            fonetized = internal.fonetize("\n".join(self.input_text.value))
            self.translation_text.value = internal.translate(fonetized, self._model.current_loaded_language).split("\n")
        else:
            self.translation_text.value = internal.detranslate("\n".join(self.input_text.value), self._model.current_loaded_language).split("\n")

    def open_language(self):
        self._model.open_language_from_file()
        self.on_text_edit()


        self.language_selector.options = [(self._model.language_pack["translator"]["nat_lang_to_gen"], 1), \
                                          (self._model.language_pack["translator"]["gen_lang_to_nat"], 2)]
        
        self.title_box.value = self._model.language_pack["translator"]["title"]
        self.instructions_box.value = self._model.language_pack["translator"]["instructions"]


    def translate_file(self):
        if self.language_selector.value == 1:
            self._model.translate_file()
        else:
            self._model.detranslate_file()



class App():
    def __init__(self) -> None:
        self.last_scene = None
        self.model = TranslatorModel()

    def demo(self, screen, scene):
        
        scenes = [
            HomeScene(screen, self.model.language_pack, name="Tab1"),
            NewLanguageScene(screen, self.model, name="Tab2"),
            Scene([TranslatorUIFrame(screen, self.model, 0)], -1, name="Tab3"),
        ]
        screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

    def run(self):
        while True:
            try:
                Screen.wrapper(self.demo, catch_interrupt=False, arguments=[self.last_scene])
                sys.exit(0)
            except ResizeScreenError as e:
                self.last_scene = e.scene

if __name__ == "__main__":
    app = App()
    app.run()
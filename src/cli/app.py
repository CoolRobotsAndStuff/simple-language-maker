#!/usr/bin/env python3

from collections import defaultdict
import sys
import random
import textwrap

from asciimatics.widgets import Frame, Layout, Divider, Button, TextBox, Widget
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

my_theme = defaultdict(
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
        self.palette = my_theme
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
    def __init__(self, screen: Screen, language_pack, language, y):
        self.language = language

        super().__init__(screen,
                         height=screen.height - y,
                         width=screen.width,
                         can_scroll=False, y=y)
        self.palette = my_theme

        self.my_screen = screen

        translator_layout = Layout([1, 1], fill_frame=True)
        self.add_layout(translator_layout)
        self.input_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True)
        self.input_text.value = language_pack["new_language"]["test_poetry"]
        translator_layout.add_widget(self.input_text, 0)

        self.translation_text = WrappedTextBox(Widget.FILL_COLUMN, line_wrap=True, readonly=True, on_change=self.on_text_edit)
        translator_layout.add_widget(self.translation_text, 1)
        self.translation_text.disabled = True
        self.translation_text.value = ["Hellooo"]

        layout1 = Layout([1])
        self.add_layout(layout1)
        layout1.add_widget(Divider())

        layout2 = TabButtons(self, 1)
        self.add_layout(layout2)
        self.fix()

    def on_text_edit(self):
        fonetized = internal.fonetize("\n".join(self.input_text.value))
        self.translation_text._reflowed_text_cache = None
        self.translation_text.value = internal.translate(fonetized, self.language).split("\n")
        self.my_screen.force_update(True)
        

class NewLanguageScene(Scene):
    def __init__(self, screen, language_pack, language, clear=True, name=None):
        title = WrappedTextBoxEffect(screen, language_pack["new_language"]["title"], screen.width - 4)
        instructions = WrappedTextBoxEffect(screen, language_pack["new_language"]["instructions"], screen.width - 4, y=title.height)
        super().__init__([title, instructions, NewLanguageUIFrame(screen, language_pack, language, y=title.height + instructions.height)], -1, clear, name)


class BravoPage(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         can_scroll=False,
                         title="Bravo Page")
        layout1 = Layout([1], fill_frame=True)
        self.add_layout(layout1)
        # add your widgets here

        layout2 = TabButtons(self, 2)
        self.add_layout(layout2)
        self.fix()


class App():
    def __init__(self) -> None:
        self.last_scene = None
        self.current_language = internal.make_random_language()
        self.language_pack = spanish(self.current_language)


    def demo(self, screen, scene):
        
        scenes = [
            HomeScene(screen, self.language_pack, name="Tab1"),
            NewLanguageScene(screen, self.language_pack, self.current_language, name="Tab2"),
            Scene([BravoPage(screen)], -1, name="Tab3"),
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
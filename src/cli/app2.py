#!/usr/bin/env python3

from asciimatics.widgets import Frame, Layout, Divider, Button
from asciimatics.scene import Scene
from asciimatics.renderers import SpeechBubble
from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
import random
import textwrap
from src import internal


class TabButtons(Layout):
    def __init__(self, frame: Frame, active_tab_idx):
        cols = [1, 1, 1]
        super().__init__(cols)
        self._frame = frame
        self._frame.set_theme('monochrome')
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


class RootPage(Frame):
    def __init__(self, screen, y):

        super().__init__(screen,
                         screen.height - y,
                         screen.width,
                         can_scroll=False, y=y)

        layout2 = TabButtons(self, 0)
        self.add_layout(layout2)
        self.fix()


class AlphaPage(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         can_scroll=False,
                         title="Alpha Page")
        layout1 = Layout([1], fill_frame=True)
        self.add_layout(layout1)
        # add your widgets here

        layout2 = TabButtons(self, 1)
        self.add_layout(layout2)
        self.fix()


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

class WrappedTextBox(Print):
    def __init__(self, screen, text, width, justify='center', uni=True, y=0, x=None):
        assert justify in ('center', 'left', 'right')
        self.text = text
        self.width = width
        self.wrapped_text, text_height = self.wrap_text(self.text, self.width, justify)
        self.height = text_height + 2
        super().__init__(screen, SpeechBubble(self.wrapped_text, uni=uni), y=y, x=x)
    
    def wrap_text(self, text: str, width, justify):
        wrapped_text = []
        for line in text.split("\n"):
            wrapped_line = textwrap.wrap(line, width, replace_whitespace=False)
            for subline in wrapped_line:
                if justify == 'left':
                    wrapped_subline = subline.ljust(width)
                elif justify == 'right':
                    wrapped_subline = subline.rjust(width)
                else:
                    wrapped_subline = subline.center(width)
                wrapped_text.append(wrapped_subline)
        
        return "\n".join(wrapped_text), len(wrapped_text)


def get_random_title():
        fonetized_name = internal.fonetize(random.choice(("Español", "lengua", "idioma")))
        fonetized_text = internal.fonetize(f"Creador de {random.choice(('Idiomas', 'Lenguajes', 'Lenguas'))} Simple")
        random_language = internal.make_random_language()
        translated_name = internal.translate(fonetized_name, random_language)
        translated_text = internal.translate(fonetized_text, random_language)
        
        return f"¡Bienvenido al Creador de Idiomas Simple! o '{translated_text}' en el idioma '{translated_name}'"


class HomePageTemplate(Scene):
    def __init__(self, screen, title_text, instructions_text, clear=True, name=None):
        title = WrappedTextBox(screen, title_text, screen.width - 4)
        instructions = WrappedTextBox(screen, instructions_text, screen.width - 4, justify='left', y=title.height)
        super().__init__([title, instructions, RootPage(screen, y=title.height + instructions.height)], -1, clear, name)

def demo(screen, scene, title_text):
    instructions_text = """¿Que deseas hacer?
⠀
* Para crear un nuevo lenguaje presiona «Nuevo»
* Para cargar un lenguage desde un archivo y traducir presiona «Traducir»
* Para salir... bueno, presiona «Salir» xd
"""
    
    scenes = [
        HomePageTemplate(screen, title_text, instructions_text, name="Tab1"),
        Scene([AlphaPage(screen)], -1, name="Tab2"),
        Scene([BravoPage(screen)], -1, name="Tab3"),
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

title_text = get_random_title()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene, title_text])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
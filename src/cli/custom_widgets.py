import textwrap
from asciimatics.widgets import TextBox
from asciimatics.effects import Print
from asciimatics.renderers import SpeechBubble
from asciimatics.strings import ColouredText

from copy import deepcopy

class WrappedTextBox(TextBox):
    def __init__(self, height, label=None, name=None, as_string=False, line_wrap=False, parser=None, on_change=None, readonly=False, justify=None, **kwargs):
        assert justify in ('center', 'left', 'right') or justify is None
        self.justify = justify
        super().__init__(height, label, name, as_string, line_wrap=line_wrap, parser=parser, on_change=on_change, readonly=readonly, **kwargs)
    
    def wrap_text(self, text: str, width, justify):
        if text is None:
            return None
        wrapped_text = []
        if type(text) == str:
            text = text.split("\n")
        
        return wrapped_text
    
    @property
    def _reflowed_text(self):
        """
        The text as should be formatted on the screen.

        This is an array of tuples of the form (text, value line, value column offset) where
        the line and column offsets are indeces into the value (not displayed glyph coordinates).
        """
        if self._reflowed_text_cache is None:
            self._reflowed_text_cache = []
            if self._line_wrap:
                limit = self._w - self._offset
                if limit == 0:
                    return self._reflowed_text_cache
                for line_index, line in enumerate(self._value):
                    if line == '':
                        wrapped_line = ['']
                    else:
                        wrapped_line = textwrap.wrap(line, limit, replace_whitespace=False, drop_whitespace=False)
                    column = 0
                    for subline_index, subline in enumerate(wrapped_line):
                        if self.justify is not None:
                            if self.justify == 'left':
                                wrapped_subline = subline.ljust(limit)
                            elif self.justify == 'right':
                                wrapped_subline = subline.rjust(limit)
                            else:
                                wrapped_subline = subline.center(limit)
                        else:
                            wrapped_subline = subline
                        
                        self._reflowed_text_cache.append((wrapped_subline, line_index, column))
                        column += len(wrapped_subline)
            else:
                self._reflowed_text_cache = [(x, i, 0) for i, x in enumerate(self._value)]

        return self._reflowed_text_cache
    

    @property
    def value(self):
        return super().value
    
    @value.setter
    def value(self, new_value):
        # Convert to the internal format
        old_value = deepcopy(self._value)
        if new_value is None:
            new_value = [""]
        elif self._as_string:
            new_value = new_value.split("\n")
        self._value = new_value

        # TODO: Sort out speed of this code
        if self._parser:
            new_value = []
            last_colour = None
            for line in self._value:
                if hasattr(line, "raw_text"):
                    value = line
                else:
                    value = ColouredText(line, self._parser, colour=last_colour)
                new_value.append(value)
                last_colour = value.last_colour
            self._value = new_value
        self.reset()

        # Only trigger the notification after we've changed the value.
        if old_value != self._value and self._on_change:
            self._on_change()
    
class WrappedTextBoxEffect(Print):
    def __init__(self, screen, text: list, width, justify='center', uni=True, y=0, x=None):
        assert justify in ('center', 'left', 'right')
        self.text = "\n".join(text)
        self.width = width
        self.wrapped_text, text_height = self.wrap_text(self.text, self.width, justify)
        self.height = text_height + 2
        super().__init__(screen, SpeechBubble(self.wrapped_text, uni=uni), y=y, x=x, speed=1)
    
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
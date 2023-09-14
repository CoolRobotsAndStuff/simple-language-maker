from dataclasses import dataclass
from pathlib import Path
import json

FILE_EXTENSION = ".slang"

@dataclass
class SimpleLanguage:
    name: str
    phoneme_circles: list

def save_to_file(location: Path, lang: SimpleLanguage):
    with open(location / Path(lang.name + FILE_EXTENSION), "w") as file:
        dictionary = dict(lang)
        json.dump(dictionary, file)

def open_from_file(file_path: Path) -> SimpleLanguage:
    with open(file_path, "r") as file:
        dictionary = json.load(file)
    return SimpleLanguage(**dictionary)
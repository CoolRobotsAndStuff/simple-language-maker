import re
from copy import copy, deepcopy
from src.internal.spanish_utils import put_accent_mark
from src.internal.simple_language import SimpleLanguage

def complete_dict(dictionary: dict) -> dict:
    dictionary = copy(dictionary)

    # Add uppercase vesions
    for key, value in copy(dictionary).items():
        dictionary[key.upper()] = value.upper()

    # Accent letters
    for key, value in copy(dictionary).items():
        accented_key = put_accent_mark(key)
        if accented_key is None:
            continue

        accented_value = put_accent_mark(value)
        if accented_value is None:
            dictionary[accented_key] = value
        else:
            dictionary[accented_key] = accented_value
    
    return dictionary

def divide_into_phonemes(text: str) -> list:
    phonemes = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "b", "d", "f", "g", "j", "k", "l", "m", "n", "ñ", "p", "rr", "(?<!r)r(?!r)", "s", "t", "v", "x", "y", "z", "ch", r"\s|\S"]

    regex = "|".join(phonemes)

    return re.findall(regex, text)

def translate(text: list, language: SimpleLanguage) -> str:
    phoneme_circles = deepcopy(language.phoneme_circles)
    replace = {}
    for circle in phoneme_circles:
        circle.reverse()
        for index in range(len(circle) -1, -1, -1):
            replace[circle[index]] = circle[index -1] 

    complete_replace = complete_dict(replace)

    #print(complete_replace)

    phoneme_list = divide_into_phonemes(text)

    for index, c in enumerate(copy(phoneme_list)):
        if c in complete_replace.keys():
            phoneme_list[index] = complete_replace[c]
            
    return "".join(phoneme_list)

def detranslate(text: list, language: SimpleLanguage):
    phoneme_circles = deepcopy(language.phoneme_circles)
    for c in phoneme_circles:
        c.reverse()
    return translate(text, phoneme_circles)

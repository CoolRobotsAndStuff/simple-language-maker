import random
from src.internal.spanish_utils import VOWELS_UNACCENTED_LOWERCASE
from src.internal.simple_language import SimpleLanguage

def make_random_language(name="my_language", excluded_phonemes=[]):
    consonant_phonemes = ["b", "d", "f", "g", "j", "k", "l", "m", "n", "ñ", "p", "r", "rr", "s", "t", "v", "y", "z", "ch"]
    vowel_phonemes = list(VOWELS_UNACCENTED_LOWERCASE)

    phoneme_groups = []
    for phoneme_set in consonant_phonemes, vowel_phonemes:
        for excluded_phoneme in excluded_phonemes:
            if excluded_phoneme in phoneme_set:
                phoneme_set.remove(excluded_phoneme)
        random.shuffle(phoneme_set)
        
        phonemes_already_divided = 0
        while True:
            phonemes_left = len(phoneme_set) - phonemes_already_divided
            if phonemes_left < 2:
                break
            group_size = random.randint(2, phonemes_left)

            group = phoneme_set[phonemes_already_divided: phonemes_already_divided+group_size]

            phonemes_already_divided += group_size
            phoneme_groups.append(group)

    return SimpleLanguage(name=name, phoneme_circles=phoneme_groups)
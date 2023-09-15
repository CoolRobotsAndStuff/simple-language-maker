import random
from src.internal.spanish_utils import VOWELS_UNACCENTED_LOWERCASE
from src.internal.simple_language import SimpleLanguage
from src.internal.fonetization import fonetize
from src.internal.translation import translate

def __generate_random_language_name(language):
    word_for_language = random.choice(("español", "lengua", "idioma", "habla"))

    return translate(fonetize(word_for_language), language)


def make_random_language(excluded_phonemes=[]):
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

    lang = SimpleLanguage(name="placeholder", phoneme_circles=phoneme_groups)
    lang.name = __generate_random_language_name(lang)

    return lang


import unicodedata
import pylabeador
from nltk.tokenize import sent_tokenize
import re

accented_characters = ("á", "é", "í", "ó", "ú")

vowels = ("a", "e", "i", "o", "u")

accented_to_non_accented = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}

def get_accented_index(syllables: list) -> int:
    
        
    if len(syllables) == 1:
        return 0
    
    last_letter = list(syllables[-1])[-1] 
    if last_letter in vowels or last_letter in ("n", "s"):
        return len(syllables) - 2

    else:
        return len(syllables) -1
    
def accentuate_syllable(syllable: str):
    non_acc_to_acc = {
        "a": "á",
        "e": "é",
        "i": "í",
        "o": "ó",
        "u": "ú",
        "A": "Á",
        "E": "É",
        "I": "Í",
        "O": "Ó",
        "U": "Ú",

    }
    if re.search(r'[áéíóúÁÉÍÓÚ]', syllable) is not None:
        return syllable
    
    vowels = list(re.finditer(r'[aeiouAEIOU]', syllable))

    if len(vowels) == 1:
        return syllable[:vowels[0].start()] + non_acc_to_acc[syllable[vowels[0].start()]] + syllable[vowels[0].end():]
    
    closed_vowels = "iuüIUÜ"
    
    #TODO dipthongs
    replace = {
        f'a(?=[{closed_vowels}])' : r'á',
        f'e(?=[{closed_vowels}])' : r'é',
        f'o(?=[{closed_vowels}])' : r'ó',
        f'(?<=[{closed_vowels}])a' : r'á',
        f'(?<=[{closed_vowels}])e' : r'é',
        f'(?<=[{closed_vowels}])o' : r'ó',
        f'(?<=[{closed_vowels}])i' : r'í',
        f'(?<=[{closed_vowels}])u' : r'ú',
        f'A(?=[{closed_vowels}])' : r'Á',
        f'E(?=[{closed_vowels}])' : r'É',
        f'O(?=[{closed_vowels}])' : r'Ó',
        f'(?<=[{closed_vowels}])A' : r'Á',
        f'(?<=[{closed_vowels}])E' : r'É',
        f'(?<=[{closed_vowels}])O' : r'Ó',
        f'(?<=[{closed_vowels}])I' : r'Í',
        f'(?<=[{closed_vowels}])U' : r'Ú',

    }

    for key, value in replace.items():
        syllable = re.sub(key, value, syllable)
    
    return syllable

def force_accent_word(word: str) -> str:
    if re.search('[áéíóúÁÉÍÓÚ]', word) is not None:
        return word
    try:
        syllables = pylabeador.syllabify(word)
    except pylabeador.HyphenatorError:
        return word
    
    accented_index = get_accented_index(syllables)

    syllables[accented_index] = accentuate_syllable(syllables[accented_index])

    return "".join(syllables)

def accent_all(base_text: str) -> str:
    spanish_characters = r'[\wáéíóúüñÁÉÍÓÚÜÑ]+'
    word_matchs = re.finditer(spanish_characters, base_text)

    for match in word_matchs:
        word = base_text[match.start():match.end()]
        base_text = base_text[:match.start()] + force_accent_word(word) + base_text[match.end():]
    
    return base_text

def fonetize_sentence(sentence: str):
    sentence = sentence.lower()
    
    replace = {
        r'(?<=\s)y(?=\s)' : "i", # 'y' to 'i'
        r'(?<![\S\s])y(?=\s)' : 'i',
        r'(?<=\s)y(?![\S\s])' : 'i',
        r'(?<![\S\s])y(?![\S\s])' : 'i',
        r'(?<!c)(h)': '', #delete "h" but not "ch"
        r'c(?=[ieíé])' : 'z', #replace 'ce' 'ci' with 'ze' 'zi'
        r'c(?!h)' : 'k', #replace lone 'c' with 'k
        r'g(?=[ieíé])' : 'j', #replace 'ge' 'gi' with 'je' 'ji'
        r'gu(?=[ieíé])' : 'g', #replace 'gue' 'gui' with 'ge' 'gi'
        r'qu' : 'k', #replace 'qu' por 'k'
        r'(?<=[aeouáéóú])y(?=\s)': 'i', #replace 'y' with 'i' when preceded by vocals (ex. muy -> mui)
        r'll' : 'y', #replace 'll' with 'y'. This varies by variety of spanish.
        r'(?<![\s])b' : 'v',  # replace 'b' with 'v' if not at the start of word
        r'(?<![\S\s])v' : 'b', # replace 'v' with 'b' if at the start of word
        r'(?<=[\s])v' : 'b', # replace 'v' with 'b' if at the start of word
        r'ü' : 'u',
        r'(?<=\s)r(?=\S)(?!r)' : 'rr', 
        r'w' : 'u',
        r'x' : 'ks',
    }
    
    for key, value in replace.items():
        sentence = re.sub(key, value, sentence)

    return sentence

def fonetize(base_text: str) -> str:
    base_text = unicodedata.normalize("NFC", base_text)

    base_text = accent_all(base_text)
    paragraphs = base_text.split("\n")
    fonetized_text = ""
    for p in paragraphs:
        sentences = sent_tokenize(p, language="spanish")

        fonetized_sentences = []
        for sentence in sentences:
            fonetized_sentences.append(fonetize_sentence(sentence))

        fonetized_text += " ".join(fonetized_sentences) + "\n"
    
    return fonetized_text


#text = fonetize("viejo Había una vez una vaca en la quebrada de humahuaca. \nEra muy vieja, muy vieja! Lingüistica, cuidate, interviur, lingüir, rápido, wálter")

#print(text)
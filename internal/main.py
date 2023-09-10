import re
import copy

import fonetization
import random

text = """Había una vez una vaca
en la Quebrada de Humahuaca.
Como era muy vieja, muy vieja,
estaba sorda de una oreja.

Y a pesar de que ya era abuela
un día quiso ir a la escuela.
Se puso unos zapatos rojos,
guantes de tul y un par de anteojos.

La vio la maestra asustada
y dijo: Estas equivocada.
Y la vaca le respondió:
¿Por qué no puedo estudiar yo?

La vaca, vestida de blanco,
se acomodó en el primer banco.
Los chicos tirábamos tiza
y nos moríamos de risa.

La gente se fue muy curiosa
a ver a la vaca estudiosa.
La gente llegaba en camiones,
en bicicletas y en aviones.

Y como el bochinche aumentaba
en la escuela nadie estudiaba.
La vaca, de pie en un rincón,
rumiaba sola la lección.

Un día toditos los chicos
se convirtieron en borricos.
Y en ese lugar de Humahuaca
la única sabia fue la vaca."""

text = fonetization.fonetize(text)


def complete_dict(dictionary: dict) -> dict:
    new_dict = {}
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
    for key, value in copy.copy(dictionary).items():
        dictionary[key.upper()] = value.upper()

    for key, value in dictionary.items():
        new_dict[key] = value
        if key in non_acc_to_acc.keys():
            try:
                new_dict[non_acc_to_acc[key]] = non_acc_to_acc[value]
            except KeyError:
                new_dict[non_acc_to_acc[key]] = value
    
    return new_dict


def translate(text: str, swaps: dict, replace: dict) -> str:
    text = fonetization.fonetize(text)

    print(text)

    complete_swaps = complete_dict(swaps)
    complete_replace = complete_dict(replace)

    for key, value in copy.copy(complete_swaps).items():
        complete_replace[value] = key
        complete_replace[key] = value

    print(complete_replace)

    character_list = list(text)

    
    for index, c in enumerate(copy.copy(character_list)):
        if c in complete_replace.keys():
            character_list[index] = complete_replace[c]
            

    return "".join(character_list)

def make_random_language(excluded_letters=[]):
    consonants = ["b", "d", "f", "g", "j", "k", "l", "m", "n", "ñ", "p", "r", "s", "t", "v", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]

    for letter in excluded_letters:
        if letter in consonants:
            consonants.remove(letter)
        elif letter in vowels:
            vowels.remove(letter)

    random.shuffle(consonants)
    random.shuffle(vowels)

    swap = {vowels[0] : vowels[1], vowels[2]: vowels[3]}
    replace = {}
    for i in range(0, len(consonants) -1, 2):
        if random.random() > 0.3:
            swap[consonants[i]] = consonants[i+1]
        else:
            replace[consonants[i]] = consonants[i+1]

    return swap, replace

"""
print(translate(text, 
                swaps={
        "o" : "e",
        "a" : "u",
        "l" : "k",
        "n" : "r",
        "m" : "v",
        "j" : "s"
    },replace = {}))
"""

swap, replace = make_random_language(excluded_letters=["x", "y", "ñ"])

print(translate(text, swap, replace))

#print(translate(translate(text)))
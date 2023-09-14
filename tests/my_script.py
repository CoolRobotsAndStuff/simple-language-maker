from src.internal.fonetization import fonetize
from src.internal import translation
from src.internal.random_language import make_random_language

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

language = make_random_language(name="my_language", excluded_phonemes=['ñ',])

print(language)

fonetic_version = fonetize(text)

print(fonetic_version)

print("-----------------------------")

translation = translation.translate(fonetic_version, language)

print(translation)


import re
import copy

import fonetization

from random_language import make_random_language


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
    # Add uppercase vesions
    for key, value in copy.copy(dictionary).items():
        dictionary[key.upper()] = value.upper()

    # Accent letters
    for key, value in dictionary.items():
        new_dict[key] = value
        if key in non_acc_to_acc.keys():
            try:
                new_dict[non_acc_to_acc[key]] = non_acc_to_acc[value]
            except KeyError:
                new_dict[non_acc_to_acc[key]] = value
    
    return new_dict


def divide_into_phonemes(text: str) -> list:
    phonemes = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "b", "d", "f", "g", "j", "k", "l", "m", "n", "ñ", "p", "rr", "(?<!r)r(?!r)", "s", "t", "v", "x", "y", "z", "ch", r"\s|\S"]

    regex = "|".join(phonemes)

    return re.findall(regex, text)


def translate(text: list, phoneme_circles: list) -> str:
    phoneme_circles = copy.deepcopy(phoneme_circles)
    replace = {}
    for circle in phoneme_circles:
        circle.reverse()
        for index in range(len(circle) -1, -1, -1):
            replace[circle[index]] = circle[index -1] 

    complete_replace = complete_dict(replace)

    #print(complete_replace)

    phoneme_list = divide_into_phonemes(text)

    for index, c in enumerate(copy.copy(phoneme_list)):
        if c in complete_replace.keys():
            phoneme_list[index] = complete_replace[c]
            
    return "".join(phoneme_list)

def detranslate(text: list, phoneme_circles: list):
    phoneme_circles = copy.deepcopy(phoneme_circles)
    for c in phoneme_circles:
        c.reverse()

    return translate(text, phoneme_circles)



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

comunism = """ La Liga Comunista, una organización obrera internacional, que en las circunstancias de la época -huelga decirlo- sólo podía ser secreta, encargó a los abajo firmantes, en el congreso celebrado en Londres en noviembre de 1847, la redacción de un detallado programa teórico y práctico, destinado a la publicidad, que sirviese de programa del partido.  Así nació el Manifiesto, que se reproduce a continuación y cuyo original se remitió a Londres para ser impreso pocas semanas antes de estallar la revolución de febrero.  Publicado primeramente en alemán, ha sido reeditado doce veces por los menos en ese idioma en Alemania, Inglaterra y Norteamérica.  La edición inglesa no vio la luz hasta 1850, y se publicó en el Red Republican de Londres, traducido por miss Elena Macfarlane, y en 1871 se editaron en Norteamérica no menos de tres traducciones distintas. La versión francesa apareció por vez primera en París poco antes de la insurrección de junio de 1848; últimamente ha vuelto a publicarse en Le Socialiste de Nueva York, y se prepara una nueva traducción.  La versión polaca apareció en Londres poco después de la primera edición alemana.  La traducción rusa vio la luz en Ginebra en el año sesenta y tantos. Al danés se tradujo a poco de publicarse.

 Por mucho que durante los últimos veinticinco años hayan cambiado las circunstancias, los principios generales desarrollados en este Manifiesto siguen siendo substancialmente exactos. Sólo tendría que retocarse algún que otro detalle. Ya el propio Manifiesto advierte que la aplicación práctica de estos principios dependerá en todas partes y en todo tiempo de las circunstancias históricas existentes, razón por la que no se hace especial hincapié en las medidas revolucionarias propuestas al final del capítulo II. Si tuviésemos que formularlo hoy, este pasaje presentaría un tenor distinto en muchos respectos. Este programa ha quedado a trozos anticuado por efecto del inmenso desarrollo experimentado por la gran industria en los últimos veinticinco años, con los consiguientes progresos ocurridos en cuanto a la organización política de la clase obrera, y por el efecto de las experiencias prácticas de la revolución de febrero en primer término, y sobre todo de la Comuna de París, donde el proletariado, por vez primera, tuvo el Poder político en sus manos por espacio de dos meses. La comuna ha demostrado, principalmente, que “la clase obrera no puede limitarse a tomar posesión de la máquina del Estado en bloque, poniéndola en marcha para sus propios fines”. (V. La guerra civil en Francia, alocución del Consejo general de la Asociación Obrera Internacional, edición alemana, pág. 51, donde se desarrolla ampliamente esta idea) . Huelga, asimismo, decir que la crítica de la literatura socialista presenta hoy lagunas, ya que sólo llega hasta 1847, y, finalmente, que las indicaciones que se hacen acerca de la actitud de los comunistas para con los diversos partidos de la oposición (capítulo IV), aunque sigan siendo exactas en sus líneas generales, están también anticuadas en lo que toca al detalle, por la sencilla razón de que la situación política ha cambiado radicalmente y el progreso histórico ha venido a eliminar del mundo a la mayoría de los partidos enumerados.

Sin embargo, el Manifiesto es un documento histórico, que nosotros no nos creemos ya autorizados a modificar.  Tal vez una edición posterior aparezca precedida de una introducción que abarque el período que va desde 1847 hasta los tiempos actuales; la presente reimpresión nos ha sorprendido sin dejarnos tiempo para eso. """

phoneme_circles = make_random_language(excluded_phonemes=["ñ"])

text = fonetization.fonetize(text)

print(phoneme_circles)

print(translate(text, phoneme_circles))

print(detranslate(translate(text, phoneme_circles), phoneme_circles))
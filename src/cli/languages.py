import random
from src import internal


def spanish(generated_language: internal.SimpleLanguage):

    word_for_language = random.choice(('Idiomas', 'Lenguajes', 'Lenguas'))
    app_name = internal.fonetize(f'Creador de {word_for_language} Simple')

    languaje_adjective = random.choice(("increíble", "hermoso", "curioso", "complejo", "interesante", "harmonioso", "bello", "difícil"))

    return  {"home":          {"title": [f"¡Bienvenido al Creador de Idiomas Simple! o '{internal.translate(app_name, generated_language)}' en el idioma '{generated_language.name}'"],
                                 "instructions": ['¿Que deseas hacer?', 
                                                  ' ', 
                                                  '* Para crear un nuevo idioma presiona «Nuevo»',
                                                  '* Para cargar un idioma desde un archivo y traducir presiona «Traducir»',
                                                  '* Para salir... bueno, presiona «Salir» xd']},

               "new_language":  {"title": [f'Observa el {languaje_adjective} idioma {generated_language.name}'],
                                 "instructions": ['¡Prueba de traducir lo que quieras! Puedes incluso traducir poesía.',
                                                  'Si te gusta el idioma, puedes guardarlo como un archivo. Luego puedes simplemente cargarlo en la ventana de traducir.'],
                                 
                                 "test_poetry": ['Había una vez una vaca',
                                                'en la Quebrada de Humahuaca.',
                                                'Como era muy vieja, muy vieja,',
                                                'estaba sorda de una oreja.',
                                                ' ',
                                                'Y a pesar de que ya era abuela',
                                                'un día quiso ir a la escuela.',
                                                'Se puso unos zapatos rojos,',
                                                'guantes de tul y un par de anteojos.',
                                                ' ',
                                                'La vio la maestra asustada',
                                                'y dijo: Estas equivocada.',
                                                'Y la vaca le respondió:',
                                                '¿Por qué no puedo estudiar yo?',],

                                 "new_button": ["Nuevo Idioma"],
                                 "save_button": ["Guardar como Archivo"],

                                 },
                                 
                                }

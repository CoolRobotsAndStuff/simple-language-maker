import random
from src import internal

def spanish(generated_language: internal.SimpleLanguage, loaded_language: internal.SimpleLanguage):

    word_for_language = random.choice(('Idiomas', 'Lenguajes', 'Lenguas'))
    app_name = internal.fonetize(f'Creador de {word_for_language} Simple')

    language_adjective = random.choice(("increíble", "hermoso", "curioso", "complejo", "interesante", "harmonioso", "bello", "difícil"))

    return  {   "home":          {  "title":        [f"¡Bienvenido al Creador de Idiomas Simple! o '{internal.translate(app_name, generated_language)}' en el idioma '{generated_language.name}'"],
                                    "instructions": ['Nota: es recomendable que utilizes este programa en pantalla completa.',
                                                    '',
                                                    '¿Que deseas hacer?', 
                                                    ' ', 
                                                    '* Para crear un nuevo idioma presiona «Nuevo»',
                                                    '* Para cargar un idioma desde un archivo y traducir presiona «Traducir»',
                                                    '* Para salir... bueno, presiona «Salir» xd',
                                                    '* Para ver el manual de instrucciones completo, presiona «Manual»']},

                "new_language":  {  "title":        [f'Observa el {language_adjective} idioma {generated_language.name}'],
                                    "instructions": ['¡Prueba de traducir lo que quieras! Puedes incluso traducir poesía.',
                                                    'Si te gusta el idioma, puedes guardarlo como un archivo. Luego puedes simplemente cargarlo en la ventana de traducir.'],
                                 
                                    "test_poetry":  ['Había una vez una vaca',
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
                "translator":  {    "title":        [f'Estás traduciendo el idioma {loaded_language.name}'],
                                    "instructions": ['Carga un idioma de un archivo .slang (Puedes generar uno desde la pestaña de «Nuevo»)',
                                                     '',
                                                    f'¡Prueba de traducir lo que quieras de {loaded_language.name} a español o viceversa! (Aunque la traducción de nuevo a español está en proceso de desarrollo)',
                                                     'Puedes incluso traducir poesía.',
                                                     'Escribe directamente en el traductor interactivo, o traduce un archivo de texto (.txt).'],

                                    "translation_direction": ["", "Dirección de traducción: "] , 

                                    "nat_lang_to_gen": f"español → {loaded_language.name}",
                                    "gen_lang_to_nat": f"{loaded_language.name} → español",

                                    "load_lang_button" : "Cargar idioma",
                                    "translate_file_button" : "Traducir archivo de texto (.txt)",
                                    "text_hint": ["Escribe aquí..."],

                                    },
                "file":     {       "translated_to": "traducido_a",
                                    "nat_lang_name": "español"

                                    },
                "manual":   {       "title": ["Manual de Instrucciones"],
                                    "instructions": [
                                        "El Creador de Idiomas Simple tiene dos funciones principales: la creación de idiomas y la traducción a dichos idiomas.",
                                        "",
                                        "CREANDO UN NUEVO IDIOMA",
                                        "Para empezar dirígete a la pestaña de «Nuevo», allí encontrarás dos columnas, una con un texto de prueba que puedes editar, y otra con ese texto traducido a otro idioma. Este idioma fué previamente generado de manera aleatoria.",
                                        "En esta pantalla puedes probar de traducir lo que quieras al idioma y ver si te gusta. Si no te convence, puedes presionar el botón de <Nuevo Idioma> y generar otro completamente distinto.",
                                        "",
                                        "COMO LEER EL NUEVO IDIOMA",
                                        "La ortografía de estos idiomas es como la de un castellano simplificado, donde se modifican algunas reglas:",
                                        "G: Es pronunciada siempre como en 'gato', sin excepciones.",
                                        "U: Nunca se omite su pronunciación. La palabra 'guiso', suena como 'güiso'.",
                                        "R: Se pronuncia siempre como en 'caro', incluso si está al inicio de la palabra. Cuando se quiera especificar el sonido 'RR' se escribirá así explícitamente.",
                                        "Y: Es pronunciada como normalmente lo harías en la palabra 'ya', sin importar su ubicación. Por ejemplo, para un hablante de español rioplatense, la palabra 'uy' no sonaría como 'ui', sino como 'ush'.",
                                        "",
                                        "El resto de las letras se pronuncian como en castellano convencional.",
                                        "",
                                        "COMO GUARDAR UN IDIOMA",
                                        "Si te gusta como suena el idioma y quieres poder volver a utilizarlo en el futuro, presiona el botón <Guardar como Archivo>. Allí podrás seleccionar dónde quieres guardar el idioma. El archivo se guardará con una extensión de '.slang'","Es recomendable armar una carpeta para guardar todos tus idiomas.",
                                        "",
                                        "COMO CARGAR UN IDIOMA",
                                        "Para volver a utilizar un idioma que guardaste, presiona el botón de <Traducir>. Esto te dirigirá a una nueva pestaña. Allí presiona el botón de <Cargar idioma>. Te aparecerá una ventana donde deberás seleccionar el archivo con extensión '.slang' que guardaste previamente.",
                                        "¡Genial! Ahora puedes utilizar el traductor. Ten en cuanta que también puedes traducir desde el nuevo idioma al castellano. Para eso debes seleccionar la opción que quieras en 'Dirección de traducción'.",
                                        "",
                                        "TRADUCIENDO ARCHIVOS DE TEXTO",
                                        "Quizás quieras traducir un archivo grande sin tener que copiarlo manualmente al traductor. Para hacer esto presiona el botón de <Traducir archivo de texto>.",
                                        "De allí saldrá una ventana que te permitirá cargar un archivo de texto simple (con extensión '.txt'). Cuando lo cargues te aparecerá otra ventana que te permitirá guardar el archivo traducido.",
                                        "Ten en cuenta que todo esto también depende de la opción que hayas seleccionado en 'Dirección de traducción.'",
                                        "",

                                        
                                        ]

                                    }  
                                }
                

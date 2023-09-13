def __make_upper(letters: tuple):
    return tuple([l.upper() for l in letters])

# Vowels
VOWELS_UNACCENTED_LOWERCASE         =   ('a', 'e', 'i', 'o', 'u')
VOWELS_UNACCENTED_UPPERCASE         =   __make_upper(VOWELS_UNACCENTED_LOWERCASE)
VOWELS_UNACCENTED                   =   VOWELS_UNACCENTED_LOWERCASE + VOWELS_UNACCENTED_UPPERCASE
VOWELS_ACCENTED_LOWERCASE           =   ('á', 'é', 'í', 'ó', 'ú')
VOWELS_ACCENTED_UPPERCASE           =   __make_upper(VOWELS_ACCENTED_LOWERCASE)
VOWELS_ACCENTED                     =   VOWELS_ACCENTED_LOWERCASE + VOWELS_ACCENTED_UPPERCASE
VOWELS_DIERESIS_LOWERCASE           =   ('ü',)
VOWELS_DIERESIS_UPPERCASE           =   __make_upper(VOWELS_DIERESIS_LOWERCASE)
VOWELS_DIERESIS                     =   VOWELS_DIERESIS_LOWERCASE + VOWELS_DIERESIS_UPPERCASE
VOWELS_DIACRITICS_LOWERCASE         =   VOWELS_ACCENTED_LOWERCASE + VOWELS_DIERESIS_LOWERCASE
VOWELS_DIACRITICS_UPPERCASE         =   __make_upper(VOWELS_DIACRITICS_LOWERCASE)
VOWELS_DIACRITICS                   =   VOWELS_DIACRITICS_LOWERCASE + VOWELS_DIACRITICS_UPPERCASE
VOWELS_LOWERCASE                    =   VOWELS_UNACCENTED_LOWERCASE + VOWELS_DIACRITICS_LOWERCASE
VOWELS_UPPERCASE                    =   __make_upper(VOWELS_LOWERCASE)
VOWELS                              =   VOWELS_LOWERCASE + VOWELS_UPPERCASE

# Closed and open vowels
VOWELS_OPEN_UNACCENTED_LOWERCASE    =   ('a', 'e', 'o')
VOWELS_OPEN_UNACCENTED_UPPERCASE    =   __make_upper(VOWELS_OPEN_UNACCENTED_LOWERCASE)
VOWELS_OPEN_UNACCENTED              =   VOWELS_OPEN_UNACCENTED_LOWERCASE + VOWELS_OPEN_UNACCENTED_UPPERCASE
VOWELS_OPEN_ACCENTED_LOWERCASE      =   ('á', 'é', 'ó')
VOWELS_OPEN_ACCENTED_UPPERCASE      =   __make_upper(VOWELS_OPEN_ACCENTED_LOWERCASE)
VOWELS_OPEN_ACCENTED                =   VOWELS_OPEN_ACCENTED_LOWERCASE + VOWELS_OPEN_ACCENTED_UPPERCASE
VOWELS_OPEN_LOWERCASE               =   VOWELS_OPEN_UNACCENTED_LOWERCASE + VOWELS_OPEN_ACCENTED_LOWERCASE
VOWELS_OPEN_UPPERCASE               =    __make_upper(VOWELS_OPEN_LOWERCASE)
VOWELS_OPEN                         =    VOWELS_OPEN_LOWERCASE + VOWELS_OPEN_UPPERCASE

VOWELS_CLOSED_UNACCENTED_LOWERCASE  =   ('i', 'u')
VOWELS_CLOSED_UNACCENTED_UPPERCASE  =   __make_upper(VOWELS_CLOSED_UNACCENTED_LOWERCASE)
VOWELS_CLOSED_UNACCENTED            =   VOWELS_CLOSED_UNACCENTED_LOWERCASE + VOWELS_CLOSED_UNACCENTED_UPPERCASE
VOWELS_CLOSED_ACCENTED_LOWERCASE    =   ('í', 'ú')
VOWELS_CLOSED_ACCENTED_UPPERCASE    =   __make_upper(VOWELS_CLOSED_ACCENTED_LOWERCASE)
VOWELS_CLOSED_ACCENTED              =   VOWELS_CLOSED_ACCENTED_LOWERCASE + VOWELS_CLOSED_ACCENTED_UPPERCASE
VOWELS_CLOSED_DIACRITICS_LOWERCASE  =   ('ü',)
VOWELS_CLOSED_DIACRITICS_UPPERCASE  =   __make_upper(VOWELS_CLOSED_DIACRITICS_LOWERCASE)
VOWELS_CLOSED_DIACRITICS            =   VOWELS_CLOSED_DIACRITICS_LOWERCASE + VOWELS_CLOSED_DIACRITICS_UPPERCASE
VOWELS_CLOSED_LOWERCASE             =   VOWELS_CLOSED_UNACCENTED_LOWERCASE + VOWELS_CLOSED_ACCENTED_LOWERCASE
VOWELS_CLOSED_UPPERCASE             =   __make_upper(VOWELS_CLOSED_LOWERCASE)
VOWELS_CLOSED                       =   VOWELS_CLOSED_LOWERCASE + VOWELS_CLOSED_UPPERCASE


# Consonants
CONSONANTS_LOWERCASE                =   ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                                         'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 
                                         't', 'v', 'w', 'x', 'y', 'z')
CONSONANTS_UPPERCASE                =   __make_upper(CONSONANTS_LOWERCASE)
CONSONANTS                          =   CONSONANTS_LOWERCASE + CONSONANTS_UPPERCASE
CONSONANTS_EXTENDED_LOWERCASE       =   ('b', 'c', 'ch', 'd', 'f', 'g', 'h', 
                                         'j', 'k', 'l', 'll', 'm', 'n', 'ñ',
                                         'p', 'q', 'r', 'rr', 's', 't', 'v',
                                         'w', 'x', 'y', 'z')
CONSONANTS_EXTENDED_UPPERCASE       =   __make_upper(CONSONANTS_EXTENDED_LOWERCASE)
CONSONANTS_EXTENDED                 =   CONSONANTS_EXTENDED_LOWERCASE + CONSONANTS_EXTENDED_UPPERCASE

# Letters
LETTERS_LOWERCASE                   =   VOWELS_LOWERCASE + CONSONANTS_LOWERCASE
LETTERS_UPPERCASE                   =   __make_upper(LETTERS_LOWERCASE)
LETTERS                             =   LETTERS_LOWERCASE + LETTERS_UPPERCASE
LETTERS_EXTENDED_LOWERCASE          =   VOWELS_LOWERCASE + CONSONANTS_EXTENDED_LOWERCASE
LETTERS_EXTENDED_UPPERCASE          =   __make_upper(LETTERS_EXTENDED_LOWERCASE)
LETTERS_EXTENDED                    =   LETTERS_EXTENDED_LOWERCASE + LETTERS_EXTENDED_UPPERCASE

LETTERS_UNACCENTED_LOWERCASE        =   VOWELS_UNACCENTED_LOWERCASE + CONSONANTS_LOWERCASE
LETTERS_EXTENDED_UNACCENTED_LOWERCASE = VOWELS_UNACCENTED_LOWERCASE + CONSONANTS_EXTENDED_LOWERCASE

# Alphabet
ALPHABET_LOWERCASE                  =   ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                                         'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 
                                         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
                                         'x', 'y', 'z')
ALPHABET_UPPERCASE                  =   __make_upper(ALPHABET_LOWERCASE)
ALPHABET_EXTENDED_LOWERCASE         =   ('a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g',
                                         'h', 'i', 'j', 'k', 'l', 'll', 'm', 'n',
                                         'ñ', 'o', 'p', 'q', 'r', 'rr', 's', 't',
                                         'u', 'v', 'w', 'x', 'y', 'z')
ALPHABET_EXTENDED_UPPERCASE         =   __make_upper(ALPHABET_EXTENDED_LOWERCASE)

# Numbers
ARABIC_NUMERALS                     =   ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
ROMAN_NUMERALS                      =   ('Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ',
                                         'Ⅸ', 'Ⅹ', 'Ⅺ','Ⅻ', 'Ⅼ', 'Ⅽ', 'Ⅾ', 'Ⅿ')
NUMERALS                            =   ARABIC_NUMERALS + ROMAN_NUMERALS

# Punctuation
PUNCTUATION                         =   ('.', ',', ':', ';', '—', '-', '…', 
                                         '«', '»', '"', '“', '”', "'", '‘', '’',
                                         '¿', '?', '¡', '!', 
                                         '(', ')', '[', ']', '{', '}', 
                                         '*', '/')
# Accent marks
DIACRITICS = ('´', '¨')

# Characters
CHARACTERS = LETTERS + NUMERALS + PUNCTUATION + DIACRITICS

__all_variables = dir()

for __name in __all_variables:
    if not __name.startswith('__'):
        __value = eval(__name)
        locals().update({"STR_" + __name: "".join(__value)})



if __name__ == "__main__":
    __all_variables = dir()
    for __name in __all_variables:
        # Print the item if it doesn't start with '__'
        if not __name.startswith('__'):
            __myvalue = eval(__name)
            print(__name, "=", __myvalue)
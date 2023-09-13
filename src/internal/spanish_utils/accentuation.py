def put_accent_mark(letter: str) -> str:
    accentuated = {
        "a": "á",
        "e": "é",
        "i": "í",
        "o": "ó",
        "u": "ú",
        "ü": "ǘ",
        "A": "Á",
        "E": "É",
        "I": "Í",
        "O": "Ó",
        "U": "Ú",
        "Ü": "Ǘ"
    }
    if letter in accentuated:
        return accentuated[letter]
    
    return letter
    
def remove_accent_mark(letter: str) -> str:
    deaccentuated = {
        "á" : "a",
        "é" : "e",
        "í" : "i",
        "ó" : "o",
        "ú" : "u",
        "ǘ" : "ü",
        "Á" : "A",
        "É" : "E",
        "Í" : "I",
        "Ó" : "O",
        "Ú" : "U",
        "Ǘ" : "Ü"
    }   
    if letter in deaccentuated:
        return deaccentuated[letter]
    
    return letter
    
def put_diaresis(letter: str) -> str:
    change = {
        "u" : "ü",
        "ú" : "ǘ",
        "U" : "Ü",
        "Ú" : "Ǘ",
    }
    if letter in change:
        return change[letter]
    
    return letter
    
def remove_diaresis(letter: str) -> str:
    change = {
        'ü' : 'u',
        'ǘ' : 'ú',
        'Ü' : 'U',
        'Ǘ' : 'Ú',
    }
    if letter in change:
        return change[letter]
    
    return letter
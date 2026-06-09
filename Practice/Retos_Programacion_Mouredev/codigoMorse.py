"""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "-", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '"': '.-..-.', '/': '-..-.'
}


VOCABULARY = {v: k.lower() for k, v in MORSE.items()}


def to_morse(string: str) ->str:
    data = []
    for palabra in string.upper().split():
        letras = [MORSE[letra] for letra in palabra if letra in MORSE]
        data.append(" ".join(letras))

    return "   ".join(data)

def from_morse(string: str)-> str:
    
    data = []
    palabras = string.lower().split("  ")

    for i in palabras:
        letras = i.split()

        for letra in letras:
            if letra in VOCABULARY:
                data.append(VOCABULARY[letra])
        data.append(' ')

    return "".join(data).strip()
    


def traductor_automatico(string:str)-> str:
    
    if string and string[0] in '.-':
        return(from_morse(string))
    else:
        return(to_morse(string))
    

print(traductor_automatico('esto es la prueba'))
print(traductor_automatico('. ... - ---   . ...   .-.. .-   .--. .-. ..- . -... .-'))


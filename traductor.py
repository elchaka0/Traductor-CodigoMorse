print('''
        ╔─────────────────────────────────────────╗
        |        TRADUCTOR DE CODIGO MORSE        |
        ╠─────────────────────────────────────────╣             
        | [1]    : Convertir texto a codigo morse |
        | [2]    : Convertir codigo morse a texto |   
        ╚─────────────────────────────────────────╝
''')



texto = ""
morse = ""

def obtener_decision():
    while True:
        try:
            decision = int(input("seleccione una opcion: "))
            if decision in [1,2]:
                return decision
            else:
                print('opcion invalida, ingrese 1 o 2.')
        except ValueError:
            print('ingrese un numero.')

decision = obtener_decision()

if decision == 1:
    texto = input('introduzca el texto: ').lower()
elif decision == 2:
    morse = input('introduzca el codigo: ')    



morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
    'z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.', '¿': '..-.-',
    '¡': '--...-', '"': '.-..-.'
}

reverse_morse_dict = {value: key for key, value in morse_dict.items()}

if decision == 1:
    texto_a_morse = ' '.join(morse_dict[char] for char in texto if char in morse_dict)
    print(f"morse: {texto_a_morse}")
elif decision == 2:
    morse_a_texto = ''.join(reverse_morse_dict[char] for char in morse.split() if char in reverse_morse_dict)
    print(f"texto: {morse_a_texto}")


while True:
    guardar = input("quiere guardar su traduccion en un archivo? (si/no): ")
    if guardar == 'si':
        nombre_archivo = input('elija el nombre del archivo(sin extension): ') + '.txt'
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            if decision == 1:
                archivo.write(texto_a_morse)
            elif decision == 2:
                archivo.write(morse_a_texto)
        print(f'archivo guardado en {nombre_archivo}')        
        break
    elif guardar == 'no':
        break
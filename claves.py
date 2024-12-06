import random
import string

def generar_contrasena():
    
    letras = string.ascii_letters
    letras += string.ascii_lowercase
    numeros = string.digits

    cadena_letras = random.choices(letras, k=3)
    cadena_numeros = random.choices(numeros, k=3)

    contrasena = ''.join(cadena_letras + cadena_numeros).capitalize() + "."

    return contrasena



print(generar_contrasena())

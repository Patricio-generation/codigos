import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_especiales):
    caracteres = string.ascii_lowercase  # Letras minúsculas
    
    if usar_mayusculas:
        caracteres += string.ascii_uppercase  # Añadir mayúsculas
    if usar_numeros:
        caracteres += string.digits  # Añadir números
    if usar_especiales:
        caracteres += string.punctuation  # Añadir caracteres especiales

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Interacción con el usuario
print("¡Bienvenido al generador de contraseñas!")
longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))
usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

# Generar y mostrar contraseña
contraseña = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_especiales)
print(f"Tu contraseña generada es: {contraseña}")
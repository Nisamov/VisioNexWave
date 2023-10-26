import random
import string

def genid_groups():#id para grupos
    # Generar 12 letras al azar (sin 'ñ')
    letters = ''.join(random.choice(string.ascii_letters.replace('ñ', '') + string.ascii_uppercase) for _ in range(12))

    # Generar tres números al azar
    numbers = ''.join(random.choice(string.digits) for _ in range(3))

    # Generar una letra mayúscula al azar
    uppercase_letter = random.choice(string.ascii_uppercase)

    # Combinar las partes para crear el código único
    unique_code = f"{letters}{numbers}.{uppercase_letter}"

    return unique_code

def genid_user():#id usuarios
    # Generar 12 letras al azar (sin 'ñ')
    letters = ''.join(random.choice(string.ascii_letters.replace('ñ', '') + string.ascii_uppercase) for _ in range(12))

    # Generar tres números al azar
    numbers = ''.join(random.choice(string.digits) for _ in range(3))

    # Generar una letra mayúscula al azar
    uppercase_letter = random.choice(string.ascii_uppercase)

    # Combinar las partes para crear el código único
    unique_code = f"{letters}{numbers}.{uppercase_letter}"

    return unique_code
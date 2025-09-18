import time
contraseña="abc"
alfabeto = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*()-_+=[]{};:,.<>/?|~`"
)
intentos=0
encontrado = False
tiempo_inicio = time.time()

def probar(cadena):
    global intentos, encontrado
    intentos += 1
    if cadena == contraseña:
        return cadena
    if len(cadena) < len(contraseña):
        for letra in alfabeto:
            resultado = probar(cadena + letra)
            if resultado:
                return resultado
    return None

posible = probar("")
tiempo_total = time.time() - tiempo_inicio

if posible:
    print("Contraseña encontrada:", posible)
    print("Intentos:", intentos)
    print(f"Tiempo total: {tiempo_total:4f}")
else:
    print("No se encontró la contraseña")
    print("Intentos:", intentos)
    print("Tiempo (s):", tiempo_total)

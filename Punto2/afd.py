import sys

def validar_id(entrada):
    estado = 'q0'

    for c in entrada:
        if estado == 'q0':
            if c.isalpha():
                estado = 'q1'
            else:
                return "NO ACEPTE"
        elif estado == 'q1':
            if c.isalnum():
                estado = 'q1'
            else:
                return "NO ACEPTE"

    if estado == 'q1':
        return "ACEPTE"
    else:
        return "NO ACEPTE"

archivo_pruebas = sys.argv[1]

try:
    with open(archivo_pruebas, "r") as archivo:
        for linea in archivo:
            prueba = linea.strip()
            if prueba:
                resultado = validar_id(prueba)
                print(f"{prueba}: {resultado}")
except FileNotFoundError:
    print(f"Error: el archivo '{archivo_pruebas}' no existe.")

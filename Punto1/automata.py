import sys

def leer(archivo):
    with open(archivo, "r") as f:
        lineas = [l.strip() for l in f if l.strip()]

    estados = lineas[0].split(",")
    alfabeto = lineas[1].split(",")
    inicial = lineas[2].strip()
    finales = lineas[3].split(",")

    transiciones = {}
    for linea in lineas[4:]:
        origen, simbolo, destino = linea.split(",")
        transiciones[(origen.strip(), simbolo.strip())] = destino.strip()

    return estados, alfabeto, inicial, finales, transiciones


def procesar_cadena(cadena, inicial, finales, transiciones):

    if cadena == "":
        return inicial in finales
        
    estado = inicial
    for simbolo in cadena:
        if (estado, simbolo) in transiciones:
            estado = transiciones[(estado, simbolo)]
        else:
            return False
    return estado in finales


def main():
    conf_file = sys.argv[1]
    cadenas_file = sys.argv[2]

    estados, alfabeto, inicial, finales, transiciones = leer(conf_file)

    with open(cadenas_file, "r") as f:
        cadenas = [l.strip("\n") for l in f]

    for c in cadenas:
        if procesar_cadena(c, inicial, finales, transiciones):
            print(f"{c} -> acepta")
        else:
            print(f"{c} -> NO acepta")


if __name__ == "__main__":
    main()

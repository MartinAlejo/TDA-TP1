import csv

# Dada una lista con monedas, devuelve con cuanto gano sofia el juego
def juego_monedas(monedas):
    turno = 0 # Los turnos pares son de Sofia, los impares de Mateo
    i = 0
    j = len(monedas) - 1

    acum_sofia = 0
    acum_mateo = 0
    while not i > j:
        moneda1 = monedas[i]
        moneda2 = monedas[j]
        if turno % 2 == 0:
            if moneda1 > moneda2:
                acum_sofia += moneda1
                i += 1
            else:
                acum_sofia += moneda2
                j -= 1
        else:
            if moneda1 < moneda2:
                acum_mateo += moneda1
                i += 1
            else:
                acum_mateo += moneda2
                j -= 1
        turno += 1

    return acum_sofia

# Dado un archivo csv, devuelve una lista con las monedas
def obtener_monedas(path, delimiter):
    monedas = []
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        next(csv_reader) # para saltear el comentario que esta al principio de los ejemplos. TODO: Quiza quitar
        for l in csv_reader:
            monedas = [int(moneda) for moneda in l]
    return monedas

def main(path):
    monedas = obtener_monedas(path, ";")
    acum_sofia = juego_monedas(monedas)
    print(acum_sofia)

main("./ejemplos/20.txt")

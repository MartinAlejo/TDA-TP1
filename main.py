import csv
import sys

# Dada una lista con monedas, devuelve una lista con los movimientos y las puntuaciones, asegurandose
# de que se Sophia siempre gana el juego
def juego_monedas(monedas):
    turno = 0 # Los turnos pares son de Sophia, los impares de Mateo
    i = 0
    j = len(monedas) - 1

    acum_sophia = 0
    acum_mateo = 0
    movimientos = []
    while not (i > j):
        primera_moneda = monedas[i]
        ultima_moneda = monedas[j]
        if turno % 2 == 0:
            if primera_moneda > ultima_moneda:
                acum_sophia += primera_moneda
                i += 1
                movimientos.append("Primera moneda para Sophia")
            else:
                acum_sophia += ultima_moneda
                j -= 1
                movimientos.append("Última moneda para Sophia")
        else:
            if primera_moneda < ultima_moneda:
                acum_mateo += primera_moneda
                i += 1
                movimientos.append("Primera moneda para Mateo")
            else:
                acum_mateo += ultima_moneda
                j -= 1
                movimientos.append("Última moneda para Mateo")
        turno += 1

    return movimientos, acum_sophia, acum_mateo

# Dado un archivo csv, devuelve una lista con las monedas
def obtener_monedas(path, delimiter):
    monedas = []
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        for l in csv_reader:
            monedas = [int(moneda) for moneda in l]
    return monedas

def main(path):
    monedas = obtener_monedas(path, ";")
    movimientos, acum_sophia, acum_mateo = juego_monedas(monedas)

    print("Suma total de monedas: " + str(sum(monedas)))
    print("Ganancia de Sophia: " + str(acum_sophia))
    print("Ganancia de Mateo: " + str(acum_mateo))
    print("Movimientos: " + "; ".join(movimientos))

if __name__ ==  '__main__':
    path = sys.argv[1]
    main(path)

# Ejemplo de ejecucion:
# python3 main.py ./ejemplos/20.txt
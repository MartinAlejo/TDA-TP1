import csv

# Dada una lista con monedas, devuelve una lista de movimientos y con cuanto gano Sophia el juego
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

    return movimientos, acum_sophia

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
    movimientos, acum_sophia = juego_monedas(monedas)
    print("; ".join(movimientos))
    print("Ganancia de Sophia: " + str(acum_sophia))

# TODO: Borrar cuando terminemos
# main("./ejemplos/20.txt")
# main("./ejemplos/25.txt")
# main("./ejemplos/50.txt")
# main("./ejemplos/100.txt")
# main("./ejemplos/1000.txt")
# main("./ejemplos/10000.txt")
# main("./ejemplos/20000.txt")
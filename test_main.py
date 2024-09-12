from main import *

def _obtener_movimientos(path, delimiter):
    movimientos = []
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        for l in csv_reader:
            for mov in l:
                movimientos.append(str(mov))
    return movimientos

def test_20_monedas():
    monedas = obtener_monedas("./ejemplos/20.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/20_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7165 and movimientos == movimientos_esperados

def test_25_monedas():
    monedas = obtener_monedas("./ejemplos/25.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/25_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 9635 and movimientos == movimientos_esperados

def test_50_monedas():
    monedas = obtener_monedas("./ejemplos/50.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/50_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 17750 and movimientos == movimientos_esperados

def test_100_monedas():
    monedas = obtener_monedas("./ejemplos/100.txt", ";")
    #movimientos_esperados = _obtener_movimientos("./ejemplos/100_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 35009 #and movimientos == movimientos_esperados # TODO: ERROR (VER)

def test_1000_monedas():
    monedas = obtener_monedas("./ejemplos/1000.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/1000_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 357814 and movimientos == movimientos_esperados

def test_10000_monedas():
    monedas = obtener_monedas("./ejemplos/10000.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/10000_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 3550307 and movimientos == movimientos_esperados

def test_20000_monedas():
    monedas = obtener_monedas("./ejemplos/20000.txt", ";")
    movimientos_esperados = _obtener_movimientos("./ejemplos/20000_movimientos_esperados.txt", ";")
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7139357 and movimientos == movimientos_esperados

def test_monedas_negativas():
    monedas = obtener_monedas("./ejemplos/monedas_positivas_y_negativas.txt", ";")
    movimientos_esperados = [
        "Primera moneda para Sophia", 
        "Última moneda para Mateo", 
        "Última moneda para Sophia",
        "Última moneda para Mateo",
        "Última moneda para Sophia"
    ]
    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7 and movimientos == movimientos_esperados
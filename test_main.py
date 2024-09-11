from main import *

def test_20_monedas():
    monedas = obtener_monedas("./ejemplos/20.txt", ";")
    movimientos_esperados = [ # TODO: Usar un archivo en vez de escribirlo asi
        "Última moneda para Sophia",
        "Primera moneda para Mateo",
        "Última moneda para Sophia",
        "Primera moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Primera moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo",
        "Primera moneda para Sophia",
        "Última moneda para Mateo"
    ]

    movimientos, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7165 and movimientos == movimientos_esperados

def test_25_monedas():
    monedas = obtener_monedas("./ejemplos/25.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 9635

def test_50_monedas():
    monedas = obtener_monedas("./ejemplos/50.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 17750

def test_100_monedas():
    monedas = obtener_monedas("./ejemplos/100.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 35009

def test_1000_monedas():
    monedas = obtener_monedas("./ejemplos/1000.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 357814

def test_10000_monedas():
    monedas = obtener_monedas("./ejemplos/10000.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 3550307

def test_20000_monedas():
    monedas = obtener_monedas("./ejemplos/20000.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7139357

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
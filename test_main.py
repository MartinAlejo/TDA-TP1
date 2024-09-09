from main import *

def test_20_monedas():
    monedas = obtener_monedas("./ejemplos/20.txt", ";")
    _, acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7165

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

## MAIN TEST ##

def test_main():
    # TODO: Probar los movimientos
    test_20_monedas()
    test_25_monedas()
    test_50_monedas()
    test_100_monedas()
    test_1000_monedas()
    test_10000_monedas()
    test_20000_monedas()

test_main()
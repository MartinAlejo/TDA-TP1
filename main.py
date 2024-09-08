def main():
    # with open("./ejemplos/20.txt", "r") as archivo:
    arr = [72,165,794,892,880,341,882,570,679,725,979,375,459,603,112,436,587,699,681,83]
    #arr = [406,691,451,628,950,324,906,34,345,647,589,585,728,338,598,362,999,227,248,863,852,344,166,153,778]
    #arr = [783,914,682,132,161,875,762,779,915,529,276,252,482,519,415,533,14,628,695,874,180,571,764,763,272,770,307,431,226,20,735,229,22,414,825,857,169,840,242,325,564,481,342,308,610,780,528,912,915,542]
    turno = 0 # turno par sofia, impar mateo

    i = 0
    j = len(arr) - 1

    sumatoria_sofia = 0
    sumatoria_mateo = 0
    while not i > j:
        moneda1 = arr[i]
        moneda2 = arr[j]
        if turno % 2 == 0:
            if moneda1 > moneda2:
                sumatoria_sofia += moneda1
                i += 1
            else:
                sumatoria_sofia += moneda2
                j -= 1
        else:
            if moneda1 < moneda2:
                sumatoria_mateo += moneda1
                i += 1
            else:
                sumatoria_mateo += moneda2
                j -= 1
        turno += 1

    print(sumatoria_sofia)

main()

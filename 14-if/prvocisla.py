while True:
    n = int(input("Zadaj N (pre ukocenie zadaj 0):"))
    for cislo in range(2, (n // 2) + 1):
        pocet = 0
        for delitel in range(1, cislo+1):
            if cislo % delitel == 0:
                pocet+= 1
        if pocet == 2:
            print(cislo, end=" ")
    print()
    if cislo == 0:
        break
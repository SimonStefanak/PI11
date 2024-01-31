def sucet(x, y):
    return x + y
def parne(cislo):
    a = 10
    if cislo % 2 == 0:
        return "párne"
    else:
        return "nepárne"

def prvocislo(cislo):
    prvocis = True
    for i in range(2, cislo):
        if cislo % i == 0:
            prvocis = False
    return prvocis


a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))
sucet = sucet(a, b)
print(f"Súčet čísel {a} + {b} = {sucet}")
print(f"Číslo {a} je {parne(a)}")
print(f"Číslo {b} je {parne(b)}")
print(f"Číslo {a} {prvocislo(a)}")
print(f"Číslo {b} {prvocislo(b)}")
if prvocis(a):
    print(f"Číslo {a} je prvočíslo!")
else:
    print(f"Číslo {a} je prvočíslo!")
if prvocis(b):
    print(f"Číslo {b} je prvočíslo!")
else:
    print(f"Číslo {b} je prvočíslo!")
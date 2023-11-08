
a = int(input("zadaj cislo a:"))
b = int(input("zadaj cislo b:"))
c = int(input("zadaj cislo c:"))
if a == b == c:
    print("cisla sa rovnaju")
else:
    if a == b:
            print("a a b sa rovnaju")
    else:
        if a == c:
            print("a a c sa rovnaju")
        else:
            if b == c:
                print ("b a c sa rovnaju")
            else:
                if a > b:
                    if a > c:
                        print("cislo a je najvacsie")
                    else:
                        print("cislo c je najvacsie")
                else:
                    if b > c:
                        print ("cislo b je najvacsie")
                    else:
                        print ("cislo c je najvacsie")
"""
a = int(input("zadaj cislo a:"))
b = int(input("zadaj cislo b:"))
c = int(input("zadaj cislo c:"))
d = int(input("zadaj cislo d:"))
e = int(input("zadaj cislo e:"))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print ("najvacsie cislo je", max)
"""
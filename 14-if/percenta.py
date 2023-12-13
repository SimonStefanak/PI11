percenta = int(input("zadaj precentá: "))

if percenta >= 90:
    print("Výborný")
else:
    if percenta >=75:
        print("Chválitebný")
    else:
        if percenta >=50:
            print("Dobrý")
        else:
            if percenta >= 30:
                print("Dostatočný")
            else:
                print("Nedostatočný!!!")

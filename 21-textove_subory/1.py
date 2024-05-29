fmena = open("mena.txt", "r", encoding="utf-8") #otvori subou mena.txt na citanie r-citanie, w-zapis, utf-8 pre znaky ktore sa normalne nevypisu
while True:
    riadok = fmena.readline()
    if riadok == "":
        break
    print(riadok[:-1]) # [:-1] vypise vsetky znaky od nulteho po predposledny




fmena.close() #zatvoremie suboru, vzdy treba!!!
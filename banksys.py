
f = open("saldo.txt", "r")
#soldot tilldelas en random mängd pengar
saldo = int(f.read())
f.close()


#banken frågar om lösenordet. lösenordet är lösen
print("Välkommen till bank.")
login = input("Snälla skriv in ditt lösenord: ")


#här räknar den ut om man skrev rätt lösenord
if login == "lösen":
    print("Välkommen till ditt konto")
else:
    print("Fel lösenord. Snälla försök igen senare.")


#här får man välja vad man vill göra i banken
meny ="q"

while meny != "a":
    try:

        print("Ditt saldo är: " + str(saldo) + "kr")
        meny = input("Vad vill du välja.[i]nsättning--[u]ttag--[a]vsluta: ")

        if meny == "i":
            insatt = int(input("Hur mycket vill du sätta in?: "))
            saldo += insatt
            print("Du satt in " + str(insatt) + "kr")


        elif meny == "u":
            utdrag = int(input("Hur mycket vill du ta ut?: "))
            saldo -= utdrag

            if saldo < 0:
                print("Du har inte tillräckligt med pengar för det där.")
                saldo += utdrag

            else:
                print("du tog ut " + str(utdrag) + "kr")


    except:
        print("det där funkar inte. prova igen.")

print("Ha en trevlig dag.")

f = open("saldo.txt" , "w")
f.write(str(saldo))
f.close()
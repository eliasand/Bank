#Här öppnas en saldo.txt
f = open("saldo.txt", "r")
saldo = int(f.read())
f.close()


#banken frågar om lösenordet. lösenordet är lösen
print("Välkommen till bank.")
login = input("Snälla skriv in ditt lösenord: ")


#här räknar den ut om man skrev rätt lösenord
try:
    if login == "lösen":
        print("Välkommen till ditt konto")
    else:
        print("Fel lösenord. Snälla försök igen senare.")
except:
    print("fel lösen")

#här får man välja vad man vill göra i banken
meny ="q"
#whileloop för flera transaktioner
while meny != "a":
    try:

        print("Ditt saldo är: " + str(saldo) + "kr")
        meny = input("Vad vill du välja.[i]nsättning--[u]ttag--[a]vsluta: ")

        #Här är insättningen av pengar
        if meny == "i":
            insatt = int(input("Hur mycket vill du sätta in?: "))
            saldo += insatt
            print("Du satt in " + str(insatt) + "kr")

        #Här är utdrag av pengar
        elif meny == "u":
            utdrag = int(input("Hur mycket vill du ta ut?: "))
            saldo -= utdrag
            #Om man inte har tillräckligt med pengar dras pengarna tillbaka
            if saldo < 0:
                print("Du har inte tillräckligt med pengar för det där.")
                saldo += utdrag
            #Pengarna drogs rätt
            else:
                print("du tog ut " + str(utdrag) + "kr")

    #Om något gick fel kommer denna print
    except:
        print("det där funkar inte. prova igen.")

#Ett trevligt hejdå när programmet stängs av
print("Ha en trevlig dag.")

#saldon uppdateras med det nya saldot
f = open("saldo.txt" , "w")
f.write(str(saldo))
f.close()
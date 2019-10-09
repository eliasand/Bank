#importerar moduler
import time

#Här öppnas en saldo.txt
s = open("saldo.txt", "r")
saldo = int(s.read())
s.close()

print("Välkommen till bank.")

#här görs och loggar man in på en användare
inlog = False
while inlog == False:
    start = str(input("ny [a]nvändare eller [l]ogga in: "))

    #Här skapar man en användare med användarnamn och pin
    if start == "a":
        print("skapar ny användare")
        loggUser = str(input("Användarnamn: "))
        loggPin = input("Pin: ")
        print("Ny användare skapad.")


    elif start == "l":
        print("Välkommen till att logga in.")
        user = str(input("Användare: "))
        pin = input("Pin: ")

        if loggUser != user:
            print("Fel användare. Något gick fel.")
        elif loggPin != pin:
            print("Fel pin. Något gick fel.")
        else:
            print("Välkommen in " + user)
            inlog = True



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
time.sleep(2)
#saldon uppdateras med det nya saldot
s = open("saldo.txt" , "w")
s.write(str(saldo))
s.close()

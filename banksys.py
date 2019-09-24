import random

saldo = random.randint(0,10000)

print("Välkommen till bank.")
login = input("Snälla skriv in ditt lösenord: ")

if login == "lösen":
    print("Välkommen till ditt konto")
else:
    print("Fel lösenord. Snälla försök igen senare.")

meny ="q"

while meny != "a":
    print("Ditt saldo är: " + str(saldo) + "kr")
    meny = input("Vad vill du välja.[i]nsättning--[u]ttag--[a]vsluta: ")
    if meny == "i":
        insätt = float(input("Hur mycket vill du sätta in?: "))
        saldo += insätt
    elif meny == "u":
        utdrag = float(input("Hur mycket vill du ta ut?: "))
        saldo -= utdrag
    else:
        print("Ha en trevlig dag.")    

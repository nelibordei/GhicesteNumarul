import random

numar_secret = random.randint(1, 10)

print("Salut, Neli! Eu m-am gandit la un numar intre 1 si 10!")
print("Poti sa-l ghicesti?")

ghicit = False

while ghicit == False:
    incercare = int(input("Scrie numarul tau: "))

    if incercare == numar_secret:
        print("BRAVOOO! Ai ghicit! Esti cea mai tare!")
        ghicit = True
    elif incercare < numar_secret:
        print("Numarul meu e mai MARE! Incearca din nou!")
    else:
        print("Numarul meu e mai MIC! Incearca din nou!")

print("Joc terminat! Te iubesc, programatoarea mea!")
# Import
from util.traitement import IP
from util.ip import *


print("Valide")
print("**********")

ip = IP("1.255.255.2")
print("1.255.255.2")
# ---------------------------------------------------------------------------------------------

if ip.getCharClasse() == 'G':
    print("L'adresse avec comme premier octet: 127 est réservé")
elif ip.getCharClasse() == 'F':
    print("L'adresse entrée n'est pas valide")
else:
    print("si c'est en classfull, la classe est la classe: ", ip.getCharClasse())
    if ip.getNbMachine() != 0:
        print("Le nombre de machines pour cette classe est: ", ip.getNbMachine())
        print("Le nombre de reseaux pour cette classe est: ", ip.getNbReseau())
    else:
        print("Cette classe n'est pas faite pour adresser des hôtes")
private = ip.charclasse
print(private)
# IP("130.255.255.2")
# IP("127.255.255.2")
# IP("115.255.255.2")
# IP("200.255.255.2")
# IP("230.255.255.2")
# IP("250.255.255.2")
# IP("225.255.255.255")

# print("Pas Valide")
# print("***************")

# IP("225.;.255.255")
# IP("22.255.255.bleu")
# IP("0.255.255.255")

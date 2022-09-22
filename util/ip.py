from .traitement import *


def toBinaire(adresse):
    binAdresse = "0b"
    for i in range(7, -1, -1):
        if (adresse >= pow(2, i)):
            adresse -= pow(2, i)
            binAdresse += "1"
        else:
            binAdresse += "0"
    return binAdresse


def stringtonumber(adresse):
    # Création de liste et assignation du premier octet
    octet = [int(adresse[0:adresse.find(".")])]
    adresse = adresse[(adresse.find(".") + 1):]

    # Second octet
    octet.append(int(adresse[0:adresse.find(".")]))
    adresse = adresse[(adresse.find(".") + 1):]

    # Troisième octet
    octet.append(int(adresse[0:adresse.find(".")]))
    adresse = adresse[(adresse.find(".") + 1):]

    # Quatrième octet
    octet.append(int(adresse[0:]))

    return octet


def verification(element):
    valid_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    for c in element:
        if valid_char.__contains__(c):
            pass
        else:
            return False
    return True


def getFirstIP(ip, masque, action):
    masqueBinaire = toBinaire(masque)
    ipChange = toBinaire(ip)
    ipChange = list(ipChange)  # Conversion en liste pour modification

    if masque == 255:
        return ip
    elif masque == 0 or action == 1:
        return 0
    else:
        for i in range(9, 1, -1):
            if (int(masqueBinaire[i]) == 0):
                ipChange[i] = 0

        # Passage en string
        ipChange = ''.join(str(v) for v in ipChange)

        return int(ipChange, 2)


def getLastIP(ip, masque, action):
    # 1 = Classique
    # 2 = CIDR

    masqueBinaire = toBinaire(masque)
    ipChange = toBinaire(ip)
    ipChange = list(ipChange)  # Conversion en liste pour modification

    if masque == 255:
        return ip
    elif masque == 0 or action == 1:
        return 255
    else:
        for i in range(9, 1, -1):
            if (int(masqueBinaire[i]) == 0):
                ipChange[i] = 1

        # Passage en string
        ipChange = ''.join(str(v) for v in ipChange)

        return int(ipChange, 2)


def limite(adresse, masque, octet):
    valid_masque = [0]
    tmp = list("0b00000000")
    for i in range(0, 8, 1):
        tmp[i + 2] = 1
        valid_masque.append(int(''.join(str(v) for v in tmp), 2))
    if (octet == 1):
        if (adresse > 223 and adresse <= 255):
            print("Les classes E et D ne sont pas autorisés.")
            return True
        elif (adresse > 255):
            print("Adresse éronée.")
            return True
    elif (octet == 2 or octet == 3):
        if (adresse > 255):
            print("Adresse éronée.")
            return True
    else:
        if (adresse == 255):
            print("Il n'est pas autorisé d'utiliser 255.")
            return True
    if(masque > 255):
        return True
    else:
        if valid_masque.__contains__(masque):
            pass
        else:
            return True

    return False

def ipmask(adresseDepart, masqueDepart):
    if (verification(adresseDepart) and verification(masqueDepart)):
        pass  # Bonne adresse
    else:
        return  # Mauvaise adresse

    ip = IP(adresseDepart)

    # Mise dans un tableau les octets
    adresse = stringtonumber(adresseDepart)
    masque = stringtonumber(masqueDepart)

    for i in range(4):
        if(i != 0 and masque[i - 1] != 255 and masque[i] != 0):
            print("Erreur masque")
            return
        if(limite(adresse[i], masque[i], (i + 1))):
            print("Erreur.")
            return

    #  Réseau, Broadcast, Nb_Machine, Nb_Réseau
    classique = ["", "", 0, 0]
    cidr = ["", "", 0, 0]

    for i in range(4):
        pass
        classique[0] += str(getFirstIP(adresse[i], masque[i], 1))
        classique[1] += str(getLastIP(adresse[i], masque[i], 1))

        cidr[0] += str(getFirstIP(adresse[i], masque[i], 2))
        cidr[1] += str(getLastIP(adresse[i], masque[i], 2))

        if (masque[i] == 255):
            classique[2] += 8
        else:
            classique[2] += 0

        cidr[2] += len(toBinaire(masque[i])[2:].replace('1', ''))

        if (masque[i] == 0):
            classique[3] = 8
            cidr[3] = len(toBinaire(masque[i - 1])[2:].replace('0', ''))

        if (i < 3):
            classique[0] += "."
            classique[1] += "."

            cidr[0] += "."
            cidr[1] += "."

    classique[2] = (pow(2, classique[2]) - 2)
    classique[3] = (pow(2, classique[3]))

    cidr[2] = (pow(2, cidr[2]) - 2)
    cidr[3] = (pow(2, cidr[3]))

    print("Pour l'adresse IP : " + str(adresseDepart) + ", avec un masque de " + str(masqueDepart) + "  : ")
    print("Adresse réseau   : " + classique[0])
    print("Broadcast réseau : " + classique[1])
    print("Nombres de machines : " + str(classique[2]))
    print("Nombres de réseaux : " + str(classique[3]) + "\n")

    if (cidr[0] != classique[0] and cidr[1] != classique[1]):
        print("Adresse S-R      : " + cidr[0])
        print("Broadcast S-R    : " + cidr[1])
        print("Nombres de machines : " + str(cidr[2]))
        print("Nombres de réseaux : " + str(cidr[3]) + "\n")

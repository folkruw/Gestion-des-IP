import ipaddress

class IP:
    __ip = ""
    __nbreseau = 0
    __nbmachine = 0
    __charclasse = ''

    # rechercher les nombres entre les points
    # pour le dernier octet, il faut prendre du dernier point jusque la fin

    def __init__(self, ip):
        a = 0
        try:
            self.ip = ipaddress.ip_address(ip)
            self.tostring()
        except ValueError:
            print("L'adresse entrée n'est pas valide")

    def tostring(self):
        ipstring = str(self.ip)
        tmp = ""
        for i in ipstring[0:3]:
            if i != '.':
                tmp += i
            else:
                break
        classe = int(tmp)
        if classe == 0:
            self.charclasse = 'F'

        elif 0 < classe <= 126:
            self.charclasse = 'A'
            self.nbmachine = 16777214
            self.nbreseau = 126

        elif classe == 127:
            self.charclasse = 'G'

        elif 128 <= classe <= 191:
            self.charclasse = 'B'
            self.nbmachine = 65534
            self.nbreseau = 16384

        elif 192 <= classe <= 223:
            self.charclasse = 'C'
            self.nbmachine = 254
            self.nbreseau = 2097152

        elif 224 <= classe <= 239:
            self.charclasse = 'D'

        elif 240 <= classe <= 255:
            self.charclasse = 'E'

    def getNbMachine(self):
        return self.nbmachine

    def getNbReseau(self):
        return self.nbreseau

    def getCharClasse(self):
        return self.charclasse

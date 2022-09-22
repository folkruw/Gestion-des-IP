import sqlite3

def connectDB():
    con = sqlite3.connect("groupe5.db")

    con.close()

def createDB():
    # Définition des plages de classes
    # donnees = [("toto", 1000), ("tata", 750), ("titi", 500)]
    # Exécutions multiples
    # for donnee in donnees:
    #    curseur.execute('''INSERT INTO scores (pseudo, valeur) VALUES (?, ?)''', donnee)
    # connexion.commit()  #Ne pas oublier de valider les modifications
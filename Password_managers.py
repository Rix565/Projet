import random 
import sys 
import string,sys

try: 
    nb_caractere= int(sys.argv[1])
    comptes = sys.argv[2]
    user = sys.argv[-1]

except ValueError: 
    print("Veuillez renseigner le NOMBRE de caractere/le type de compte(facebook,insta...)/le nom d'utilisateur a la ligne de commande")
    sys.exit()
    
except IndexError: 
    print("Veuillez renseigner le nombre de caractere/le type de compte(facebook,insta...)/le nom d'utilisateur a la ligne de commande")
    sys.exit()

class Password_manager:

    def mdp(self):
        strings = string.ascii_letters+string.ascii_lowercase+string.digits+string.punctuation
        self.mdp = random.sample(strings,nb_caractere)
        self.mdp = "".join(self.mdp)
        return self.mdp

    def compte(self):
        self.comptes = comptes
        return self.comptes

    def utilisateur(self): 
        self.user = user
        return user

    def base_de_donne(self): 
        point = 0
        with open("base_de_donne.txt","a+") as file:
            file.write(f"Compte: {self.comptes} | Utilisateur : {self.user} | Mot de passe: {self.mdp} \n")

p=Password_manager()
p.mdp()
p.compte()
p.utilisateur()
p.base_de_donne()
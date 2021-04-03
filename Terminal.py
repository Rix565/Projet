import os 
import time 
class Terminal: 
    def __init__(self,name): 
        os.system("clear")
        self.name=name
        self.boucle1()

    
    def boucle1(self): 
        terminal=True
        while terminal: 
            console=input(f"{self.name}>>")
            if console == "quit": 
                print("Au revoir")
                time.sleep(3)
                terminal=False
                
            elif console == "help": 
                print("help:  Affiche toute les commande est leur utilisation")
                print("name:  Affiche le nom du terminal")
                print("clear: Nettoye le terminale")
                print("newd:  Creer un dossier")
                print("newc:  Creer un fichier")
                print("remove:  Supprime un fichier ")
                print("remove -r:  Supprime un dossier")
                print("rename:  Renomme un fichier/dossier")
                print("dr    :  lis un fichier")
            elif console == "clear": 
                os.system("clear")
                
            elif console == "name": 
                print(self.name)
                
            elif console == "newd": 
                nom_dossier=input("Entrez le nom du dossier: ")
                os.makedirs(nom_dossier)
                print("Fichier crée!")
                
            elif console == "newc": 
                nom_fichier=input("Entrez le nom du fichier: ")
                file=open(nom_fichier,"w")
                file.close()
                
            elif console == "remove":
                nom_fichier1=input("Entrez le nom du fichier a supprimer: ")
                try: 
                    os.remove(nom_fichier1)
                except: 
                    print("Fichier non existant")
            
            elif console == "remove -r": 
                nom_dossier1=input("Entrez le nom du dossier a supprimer")
                try: 
                    os.rmdir(nom_dossier1)
                except: 
                    print("Dossier non existant")
            
            elif console == "rename": 
                dossier=input("Entrez le nom du dossier/fichier a renommer: ")
                dossier1=input("Nouveau nom: ")
                try: 
                    os.renames(dossier,dossier1)
                except FileNotFoundError: 
                    print("Fichier/Dossier non existant")
                
            elif console == "dr": 
                fichier_lire=input("Nom du fichier a lire: ")
                try: 
                    file=open(f"{fichier_lire}","r")
                    file.readlines()
                    file.close()
                except FileNotFoundError: 
                    print("Fichier/Dossier non existant")
                    
            else: 
                print("Commande Introuvable")
t1=Terminal("Utilisateur")
                
            
                


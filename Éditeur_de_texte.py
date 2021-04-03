from tkinter import * 
import os

if os.name == "nt": 
    os.system("cls")
else: 
    os.system("clear")

class Application(Tk): 
    def __init__(self): 
        Tk.__init__(self)
        self.configuration()
        self.menu()
        self.editeur_texte()
        self.affichage()
        
    def configuration(self): 
        self.title("Éditeur de texte")
        self.geometry("1359x900")
        
        
    def menu(self): 
        self.menu=Menu(self)
        self.menu1=Menu(self.menu,tearoff=0)
        self.menu1.add_command(label="Nouveau")
        self.menu1.add_command(label="Ouvrir")
        self.menu1.add_command(label="Enregistrer")
        self.menu1.add_command(label="Quitter",command=self.menu.quit)
        self.menu.add_cascade(label="Fichier",menu=self.menu1)
        
        self.menu2=Menu(self.menu,tearoff=0)
        self.menu2.add_command(label="Copier")
        self.menu2.add_command(label="Coller")
        self.menu2.add_command(label="Recherche")
        self.menu.add_cascade(label="Édition",menu=self.menu2)
        
        self.menu3=Menu(self.menu,tearoff=0)
        self.menu3.add_command(label="Ajouter image")
        self.menu.add_cascade(label="Insertion",menu=self.menu3)

    def editeur_texte(self): 
        self.e=Text(self)
        
    def affichage(self):
        self.e.pack(ipadx=1000,ipady=900,padx=200)
        self.config(menu=self.menu)
        self.mainloop()

app=Application()


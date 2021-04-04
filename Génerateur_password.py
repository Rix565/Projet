import random,os,string
from tkinter import * 

class Password: 
    def __init__(self,maxi): 
        self.maxi=maxi
        self.root=Tk()
        self.root.geometry("1359x900")
        self.root.title("Génerateure de mot de passe")
        self.root.config(background="white")
        self.champs() 
        self.root.mainloop()
        os.system("clear")
        
    def generateur_mdp(self): 
        lettre=string.ascii_letters+string.punctuation+string.digits
        mdp=random.sample(lettre,self.maxi)
        password="".join(mdp)
        print(password)
        self.e1.delete(0,END)
        self.e1.insert(0,password)
        
    def champs(self): 
        f1=LabelFrame(self.root,height=300,width=300,bg="white")
        b1=Button(f1,text="CLIQUEZ POUR GÉNERER UN MOT DE PASSE",command=self.generateur_mdp)
        self.e1=Entry(f1)
        f1.pack(side="right",padx=100)
        self.e1.pack(fill="both")
        b1.pack()        
p=Password(8)
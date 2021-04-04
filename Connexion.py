import json 
import os 

def connexion(): 
    count={"admin":"admin",
        "user":"ayoubfoot68",
        "marta":"login",
        "window":"vista7"}
    c=0
    with open("C:\\Users\\ayoub\\Documents\\educadhoc\\Python\\Project\\base_de_donne.json","w") as file: 
        json.dump(count,file,indent=4)
    login=input("Identifiant: ")
    password=input("Mot de passe: ")
    for keys,values in count.items(): 
        if login in keys and password in values and not login == "" and password == "" : 
            print(f"Bienvenue {login}")
            break

connexion()

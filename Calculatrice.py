import sys

try: 
    a = int(sys.argv[1])
    operateur =  sys.argv[2]
    b = sys.argv[3]

except ValueError: 
    print("Veuillez renseigner ces element: nombre1,operateur de calcul est nombre2\n"
    "Par exemple:  12 % 2 | 12 + 09 ")
    sys.exit()

except IndexError:
    print("Veuillez renseigner ces element: nombre1,operateur de calcul est nombre2\n"
    "Par exemple:  12 % 2 | 12 + 09 ")
    sys.exit()

class Calculatrice: 
    def __init__(self):
        self.a = a
        self.operateur = operateur
        self.b = b
        self.calcule()


    def calcule(self): 
        liste=["+","-","/","*","%"]
        for i in liste: 
            if i in sys.argv: 
                self.operateur=i
        self.a=sys.argv[1]
        self.b=sys.argv[-1]

        if self.operateur == "+": 
            print(f"{int(self.a) + int(self.b)}")

        elif self.operateur == "-": 
             print(f"{int(self.a) - int(self.b)}")

        elif self.operateur == "/": 
             print(f"{int(self.a) // int(self.b)}")

        elif self.operateur == "*" : 
             print(f"{int(self.a) * int(self.b)}")

        elif self.operateur == "%": 
             print(f"{int(self.a) % int(self.b)}")


c=Calculatrice()


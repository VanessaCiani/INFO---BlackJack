class Carta:
    def __init__(self, seme: str, rango: str): #"__init__" --> COSTRUTTORE
        #Rendo i due attributi privati tramite l'utilizzo di "__"
        #Gli attributi privati possono essere modificati solo dall'interno della classe e non dall'esterno, questo passaggio serve a rendere i nostri dati più sicuri
        self.__seme = seme       
        self.__rango = rango     

    #Imposto le property per il seme e per il rango
    @property
    def seme(self):
        return self.__seme

    @property
    def rango(self):
        return self.__rango

    #Imposto la property per il valore
    @property
    def valore(self) -> int:
        #Controllo che valore numerico associare ad ogni carta
        if self.__rango in ["J", "Q", "K"]:
            return 10            
        elif self.__rango == "A":
            return 11            
        else:
            return int(self.__rango)  
        
    def __str__(self):
        #Rappresentazione testuale della carta
        return f"Seme: {self.__seme}, Valore: {self.__rango}"


        return f"Seme: {self.__seme}, Valore: {self.__rango}"

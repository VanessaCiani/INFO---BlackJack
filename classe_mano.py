class Mano:
    def __init__(self):
        #Lista vuota che conterrà le carte che avrò in mano
        self.__carte = []       
    
    def aggiungi_carta(self, carta):
        #Aggiunge una carta alla mano
        self.__carte.append(carta)

    #Imposto la property
    @property
    def get_carte(self):
        #Restituisce la lista delle carte creata in precedenza
        return self.__carte
    
    def svuota(self):
        #Rimuove tutte le carte dalla lista
        self.__carte = []

    def __str__(self):
        stringa = ""
        for carta in self.__carte:
            stringa += str(carta) + "\n"   #Converte ogni carta in stringa (INTERO --> STRINGA)
        return stringa

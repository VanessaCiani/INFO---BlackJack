import random

class Mazzo:
    def __init__(self, lista_carte):
        self.__carte = lista_carte  #Lista privata che contiene tutte le carte del mazzo

    #Imposto la property
    @property
    def carte(self):
        #Restituisce la lista delle carte
        return self.__carte

    def mescola(self):
        #Mescola le carte in modo casuale (.shuffle)
        random.shuffle(self.__carte)

    def pesca(self):
        #RImuove e restituisce l'ultima carta del mazzo (.pop)
        carta_rimossa = self.__carte.pop()
        return carta_rimossa

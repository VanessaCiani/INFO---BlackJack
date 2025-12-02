import random

class Mazzo:
    def __init__(self, lista_carte):
        self.__carte = lista_carte  #Lista privata che contiene tutte le carte del mazzo

    #Imposto la property
    @property
    def carte(self):
        #
        return self.__carte

    def mescola(self):
        # mescola le carte in modo casuale
        random.shuffle(self.__carte)

    def pesca(self):
        # rimuove e restituisce l'ultima carta del mazzo
        carta_rimossa = self.__carte.pop()
        return carta_rimossa

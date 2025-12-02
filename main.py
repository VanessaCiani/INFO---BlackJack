from classe_carta import Carta
from classe_mazzo import Mazzo
from classe_mano import Mano

if __name__ == "__main__":
    #Creazione di due liste (semi e valori)
    semi = ['♠', '♥', '♦', '♣']
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    #Generazione del mazzo da 52 carte
    carte = [Carta(seme, valore) for seme in semi for valore in valori]

    mazzo = Mazzo(carte)   #Crea un mazzo con tutte le carte
    mazzo.mescola()        #Mescola il mazzo

    mano = Mano()          #Crea una mano VUOTA

    for _ in range(5):
        #Pesca una carta dal mazzo e la aggiunge alla mano, per un totale di 5 volte
        mano.aggiungi_carta(mazzo.pesca())
        
    print("Le tue 5 carte sono:")
    print(mano)            #Stampa tutte le carte che hai in mano 

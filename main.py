from card import Card
from stack import Stack
from os import system
from random import randint

def makeSticks(card):
    return [Card(card.color, card.icon, card.stick) for _ in range(13)]

def setValueStick(cards):
    for i in range(13):
        cards[i].setValue(i + 1)

def shuffleCards(cards):
    maxLength = len(cards) - 1
    cards1 = []
    
    for _ in range(13):
        index = randint(0, maxLength)
        cards1.append(cards.pop(index))
        maxLength -= 1
        
    return cards1

def makeDeck(heards, diamonds, trevols, picas):
    deckOfCards = []
    deckOfCards.append(heards)
    deckOfCards.append(diamonds)
    deckOfCards.append(trevols)
    deckOfCards.append(picas)
    
    return deckOfCards
        
def printDeck(deckOfCards):
    for i in range(4):
        for j in range(13):
            print(deckOfCards[i][j].getStick(), end=", ")
        print()
            
if __name__ == "__main__":
    
    print("//Solitario//")
    input("[INGRESE ENTER PARA JUGAR]")
    
    endGame = False
    while not endGame:
        
        # Definir listas de cada palo, y su valor en cada posicion
        heard = Card("red", "<3", "hearts")
        heards = makeSticks(heard)
        setValueStick(heards)
        
        diamond = Card("red", "<>", "diamonds")
        diamonds = makeSticks(diamond)
        setValueStick(diamonds)
        
        trevol = Card("black", "-3", "clubs")
        trevols = makeSticks(trevol)
        setValueStick(trevols)
        
        pica = Card("black", "->", "spades")
        picas = makeSticks(pica)
        setValueStick(picas)
        
        # Revolver Cartas
        heards = shuffleCards(heards)
        diamonds = shuffleCards(diamonds)
        trevols = shuffleCards(trevols)
        picas = shuffleCards(picas)
        
        deckOfCards = makeDeck(heards, diamonds, trevols, picas)
        printDeck(deckOfCards)
        input("para")
        



        


        
        
        
    
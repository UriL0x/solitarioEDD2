from card import Card
from stack import Stack
from os import system
from random import randint

def makeStickDeck(color, icon, stick):
    card = Card(color, icon, stick)
    cards = makeSticks(card)
    setValueStick(cards)
    
    return cards

def makeSticks(card):
    return [Card(card.color, card.icon, card.stick) for _ in range(13)]

def setValueStick(cards):
    for i in range(13):
        cards[i].setValue(i + 1)

def shuffleCards(cards):
    maxLength = len(cards) - 1
    cards1 = []
    
    for _ in range(52):
        index = randint(0, maxLength)
        cards1.append(cards.pop(index))
        maxLength -= 1
        
    return cards1

def printDeck(deckOfCards):
    for i in range(len(deckOfCards)):
        print(deckOfCards[i].getValue(), end=", ")
        if i == 12 or i == 25 or i == 38:
            print()
    print()

def pushSeveral(deck, num):
    stack = Stack()
    for i in range(num):
        stack.push(deck[i])
    deleteSomeItems(deck, num)    
    
    return stack

def deleteSomeItems(deck, num):
    for i in range(num-1, -1, -1):
        deck.pop(i)
                 
if __name__ == "__main__":
    
    print("//Solitario//")
    input("[INGRESE ENTER PARA JUGAR]")
    
    endGame = False
    while not endGame:
        
        # Crear palos
        heards = makeStickDeck("red", "<3", "hearts")    
        diamonds = makeStickDeck("red", "<>", "diamonds")
        trevols = makeStickDeck("black", "-3", "clubs")    
        picas = makeStickDeck("black", "->", "spades")
    
        # Hacer baraja de solitario de cartas revueltas
        deckOfCards = heards + diamonds + trevols + picas
        deckOfCards = shuffleCards(deckOfCards)
        
        # Imprimir baraja de cartas (PRUEBAS)
        printDeck(deckOfCards)
        input("para")
        
        # Crear pila1
        stack1 = pushSeveral(deckOfCards, int(1))
        stack1.printCardStack()
        
        # Crear pila2
        stack2 = pushSeveral(deckOfCards, int(2))
        stack2.printCardStack()
        
        # Crear pila3
        stack3 = pushSeveral(deckOfCards, int(3))
        stack3.printCardStack()
        
        # Crear pila4
        stack4 = pushSeveral(deckOfCards, int(4))
        stack4.printCardStack()
        
        # Crear pila5
        stack5 = pushSeveral(deckOfCards, int(5))
        stack5.printCardStack()
        
        # Crear pila6
        stack6 = pushSeveral(deckOfCards, int(6))
        stack6.printCardStack()
        
        # Crear pila7
        stack7 = pushSeveral(deckOfCards, int(7))
        stack7.printCardStack()
        
        print("_______________")
        printDeck(deckOfCards)
        print("len: ", len(deckOfCards))
        
        # Crear pila 0 (cartas sobrantes)
        print("PILA0:")
        stack0 = pushSeveral(deckOfCards, int(24))
        stack0.printCardStack()
        print()
        
        input("stop")
    
    

    
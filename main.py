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
        
def showGameInfo(stacks):
    
    # Definir sistema de coordenadas
    width, height = 20, 20

    # Ejecutar he imprimir sistema de coordenadas
    print("+", ((width - 2) * "-"), "+")
    
    stacks[0].getTop().printCard() 
    print()
    stacks[1].getTop().printCard() 
    print()
    stacks[2].getTop().printCard() 
    print() 
    stacks[3].getTop().printCard() 
    print()
    stacks[4].getTop().printCard() 
    print()
    stacks[5].getTop().printCard() 
    print()
    stacks[6].getTop().printCard() 
    print()
    stacks[7].getTop().printCard() 
    print()    
    
    print("+", ((width - 2) * "-"), "+")
    
def checkPos(cor, num):
    if cor in num:
        return True
    return False
    
def stackToStr(stack):
    stackList = []
    for i in range(stack.getLength()):
        stackList.append(str(stack.getTop().getValue()))
        stack.pop()
    reversedStr = "".join(reversed(stackList))
        
    return reversedStr

def stackToList(stack):
    stackList = []
    while not stack.isEmpty():
        stackList.append(stack.getTop().getValue())
        stack.pop()
    
    return stackList

def checkPos(action):
    if not action == '0' or action == '1' or action == '2' or action == '3' or action == '4' or action == '5' or action == '6' or action == '7':
        return False
    return True

def moveItemTostack(stacks, action, action1):
    if action1 == '0':
        popAndPush(stacks, action, action1)
    elif action1 == '1':
        popAndPush(stacks, action, action1)
    elif action1 == '2':
        popAndPush(stacks, action, action1)
    elif action1 == '3':
        popAndPush(stacks, action, action1)
    elif action1 == '4':
        popAndPush(stacks, action, action1)
    elif action1 == '5':
        popAndPush(stacks, action, action1)
    elif action1 == '6':
        popAndPush(stacks, action, action1)
    elif action1 == '7':
        popAndPush(stacks, action, action1)
    
def popAndPush(stacks, action, action1):
    i = ord(action)
    card = stacks[i].getTop()
    stacks[i].pop()
    i = ord(action1)
    stacks[i].push(card)
                 
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
        
        # Crear pilas
        stack1 = pushSeveral(deckOfCards, int(1))
        stack2 = pushSeveral(deckOfCards, int(2))
        stack3 = pushSeveral(deckOfCards, int(3))
        stack4 = pushSeveral(deckOfCards, int(4))
        stack5 = pushSeveral(deckOfCards, int(5))
        stack6 = pushSeveral(deckOfCards, int(6))
        stack7 = pushSeveral(deckOfCards, int(7))
        
        # Crear pila 0 (cartas sobrantes)
        stack0 = pushSeveral(deckOfCards, int(24))
        
        deckStacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7]
        while True:
            showGameInfo(deckStacks)
            action = input("[SELECCIONE UNA PILA]")
            system("cls")
            showGameInfo(deckStacks)
            action1 = input("[SELECCIONE LA PILA A DONDE MOVER LA CARTA]")
            system("cls")
            
            if checkPos(action) or checkPos(action1):
                showGameInfo(deckStacks)
                print("[!]INGRESE UN DATO VALIDO")
            else:
                moveItemTostack(deckStacks, action, action1)
                
            system("cls")
    
    

    
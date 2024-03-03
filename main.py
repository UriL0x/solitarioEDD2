import copy
from card import Card
from stack import Stack
from os import system
from random import randint

def makeStickDeck(color, icon, stick):
    card = Card(color, icon, stick)
    cards = [Card(card.color, card.icon, card.stick) for _ in range(13)]
    setValueStick(cards)
    
    return cards

def setValueStick(cards):
    for i in range(13):
        if i < 9:
            value = "0" + str((i + 1))
        else:
            value = str(i + 1)
        cards[i].setValue(value)


def shuffleCards(cards):
    maxLength = len(cards) - 1
    cards1 = []
    
    for _ in range(52):
        index = randint(0, maxLength)
        cards1.append(cards.pop(index))
        maxLength -= 1
        
    return cards1

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
    # Pila0 (pila para agarrar cartas)
    print("+", ((50 * 2) * "-"), "+")
    print("| Pila0 >> " + getCardStack(stack0, 0))
    print("+", ((50 * 2) * "-"), "+")
    
    # Resto de pilas
    print("| Pila1 >> " + getCardStack(stacks[1], 1))
    print("| Pila2 >> " + getCardStack(stacks[2], 2))
    print("| Pila3 >> " + getCardStack(stacks[3], 3))
    print("| Pila4 >> " + getCardStack(stacks[4], 4))
    print("| Pila5 >> " + getCardStack(stacks[5], 5))
    print("| Pila6 >> " + getCardStack(stacks[6], 6))
    print("| Pila7 >> " + getCardStack(stacks[7], 7))
    print("+", ((50 * 2) * "-"), "+")
    
    # Mostrar pilas completadas
    print("| <3={} <>={} -3={} ->={}".format(1,1,1,1))
    print("+", ((50 * 2) * "-"), "+")
    print(stack7.getLength())
    print(stack7.getTop())
    
def getCardStack(stack, num):
    length = min(10, stack.getLength())
    
    stackStr = str()
    if not stack.isEmpty():
        stack1 = copy.deepcopy(stack)
        for i in range(length):
            stack1.getTop().setVisibility(True)
            stackStr += str(stack1.getTop().getCard())
            stack1.pop()
        return stackStr
            
    return " "
        
def checkPos(action):
    if not action == '0' or action == '1' or action == '2' or action == '3' or action == '4' or action == '5' or action == '6' or action == '7':
        return False
    return True

def playGameOptions(stacks, action, action1):
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
    
        # Hacer baraja de solitario con cartas revueltas
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
        
        stacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7]
        while True:
            showGameInfo(stacks)
            action = input("[SELECCIONE UNA PILA]")
            
            
            #system("cls")
            #showGameInfo(deckStacks)
            #action1 = input("[SELECCIONE LA PILA A DONDE MOVER LA CARTA]")
            #system("cls")
            
            #if checkPos(action) or checkPos(action1):
            #    showGameInfo(deckStacks)
            #    print("[!]INGRESE UN DATO VALIDO")
            #    playGameOptions(deckStacks, action, action1)
                
            system("cls")
    
    

    
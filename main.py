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
    
    # Mostrar pilas madre completadas pilas completadas
    heard = stacks[8].getTop().getCard()
    diamond = stacks[9].getTop().getCard()
    clubs = stacks[10].getTop().getCard()
    spades = stacks[11].getTop().getCard()
        
    print("| heards[8] >> {} diamonds[9] >> {} clubs[10] >> {} spades[11] >> {}".format(heard, diamond, clubs, spades))
    print("+", ((50 * 2) * "-"), "+")
    
def getCardStack(stack, num):
    length = min(10, stack.getLength())
    
    stackStr = str()
    if not stack.isEmpty():
        stack1 = copy.deepcopy(stack)
        for i in range(length):
            stackStr += str(stack1.getTop().getCard())
            stack1.pop()
        return stackStr
            
    return " "
        
def selectStack(message, stacks):
    showGameInfo(stacks)
    action = input(message)
    system("cls")
    
    return action

def invalidAction(message, stacks):
    showGameInfo(stacks)
    input(message)
    system("cls")
        
def checkStack(stacks, action, mode):
    if mode == '1':
        if action == '0' or action == '1' or action == '2'  or action == '3'  or action == '4'  or action == '5'  or action == '6'  or action == '7':
            return True
        else:
            False
        
    if mode == '2':
        if action == '1' or action == '2'  or action == '3'  or action == '4'  or action == '5'  or action == '6'  or action == '7':
            return True
        elif action == '8' or action == '9' or action == '10' or action == '11':
            if checkStacksCompleted(stacks):
                return False
            return True
        else:
            return False

def checkStacksCompleted(stacks):
    if stacks[8].getLength() >= 12 and stacks[9].getLength() >= 12 and stacks[10].getLength() >= 12 and stacks[11].getLength() >= 12:
        return True
    else:
        return False

def checkCardAtributes(stack, stack1):
    if stack.getTop().getValue() < stack1.getTop().getValue() and stack.getTop().getColor() != stack1.getTop().getColor():
        return True
    else:
        return False
    
def checkAllAtributes(stack, stackMother):
    card = stack.getTop()
    cardMother = stackMother.getTop()
   
    if card.getValue() < cardMother.getValue():
        if card.getStick() == cardMother.getStick():
            if card.getColor() == cardMother.getColor():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def popAndPush(stack1, stack2):
    card = stack1.getTop()
    stack1.pop()
    stack2.push(card)
    system("cls")
                 
if __name__ == "__main__":
    
    print("//Solitario//")
    option = input("a) Jugar\n"
          "b) Como se juega?")
    system("cls")
    
    if option == "b":
        print("Este juego tiene algo de especial\n"
              "las cartas estan d emanera horizontal\n"
              "para seleccionar una columa se ingresa el numero de esta\n")
        print("Pila4 >> [*|*] [*|*] [*|*] [*|*] [*|*]")
        print("\nPor lo demas se juega como el solitario normal \n"
              "Las cartas van de derecha a izquierda")
        input("[ENTER PARA JUGAR]")
    
    endProgram = False
    while not endProgram:
        
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
        
        # Crear pilas madre de cada palo
        card1 = Card("red", "<3", "hearts")
        card1.setValue(int(14))
        motherHeard = Stack()
        motherHeard.push(card1)
        card2 = Card("red", "<>", "diamonds")
        card2.setValue(int(14))
        motherDiamond = Stack()
        motherDiamond.push(card2)
        card3 = Card("black", "-3", "clubs") 
        card3.setValue(int(14))
        motherClubs = Stack()
        motherClubs.push(card3)
        card4 = Card("black", "->", "spades")
        card4.setValue(int(14))
        motherSpades = Stack()
        
        
        # Meter todas la pilas en un lista
        stacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, motherHeard, motherDiamond, motherClubs, motherSpades]
        
        playGame = True
        while playGame:
            
            # Seleccionar primera pila
            while True:
                action = selectStack("[SELECCIONA LA PRIMERA PILA]", stacks)
                if checkStack(stacks, action, '1'):
                    break    
                else:
                    invalidAction("[NUMERO DE PILA INVALIDA!!!]", stacks)
            
            # Seleccionar segunda pila
            cardToMove = stacks[int(action)].getTop().getCard()
            message = str("Carta a mover [PILA" + action + "]>>" + cardToMove + "\n[SELECCIONA LA SEGUNDA PILA]")
            while True:
                action1 = selectStack(message, stacks)
                if checkStack(stacks, action1, '2'):
                    break
                else:
                    invalidAction("[NUMERO DE PILA INVALIDA!!!]", stacks)
            
            # Llenar pilas madres de cartas
            if action1 == '8' or action1 == '9' or action1 == '10' or action1 == '11':       
                if checkAllAtributes(stacks[int(action)], stacks[int(action1)]):
                    stacks[int(action1)].push(stacks[int(action)])
                else:
                    invalidAction("[ACCION INVALIDA!!!]", stacks)
            
            # Llenar resto de pilas
            else:
                if checkCardAtributes(stacks[int(action)], stacks[int(action1)]):
                    popAndPush(stacks[int(action)], stacks[int(action1)])    
                else:
                    invalidAction("[ACCION INVALIDA!!!]", stacks)
                    
            # Comprobar si todas la pila madre estan completas
            if checkStacksCompleted(stacks):
                print("YOU WIN!!!!")
                playGame = False
                
            
    
    

    
from card import Card

class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.elements = [0] * self.MAX_SIZE
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.MAX_SIZE - 1

    def push(self, element):
        if not self.isFull():
            self.top += 1
            self.elements[self.top] = element
        else:
            print("Error: La pila está vacía")

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
        else:
           print("Error: La pila está vacía") 

    def getTop(self):
        if not self.isEmpty():
            return self.elements[self.top]
        else:
            print("Error: La pila está vacía")
            
    def getLength(self):
        return self.top + 1

    def printStack(self):
        for i in range(self.top + 1):
            print(self.elements[i], end=", ")
        print()
    
        

    
        

        
    
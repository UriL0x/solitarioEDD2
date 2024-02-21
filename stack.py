class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.elements = [0] * self.MAX_SIZE
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX_SIZE - 1

    def push(self, element):
        if not self.is_full():
            self.top += 1
            self.elements[self.top] = element
        else:
            print("Error: La pila está llena")

    def pop(self):
        if not self.is_empty():
            self.top -= 1
        else:
            print("Error: La pila está vacía")

    def get_top(self):
        if not self.is_empty():
            return self.elements[self.top]
        else:
            print("Error: La pila está vacía")

    def print_stack(self):
        print("Contenido de la pila:", end=" ")
        for i in range(self.top + 1):
            print(self.elements[i], end=", ")
        print()
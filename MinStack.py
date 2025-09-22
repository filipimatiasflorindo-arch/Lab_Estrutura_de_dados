from stack import Stack

class MinStack:
    def __init__(self):
        self.main_stack = Stack()   
        self.min_stack = Stack()    

    def push(self, value):
        self.main_stack.push(value)
    
        if self.min_stack.is_empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)

    def pop(self):
        if self.main_stack.is_empty():
            raise IndexError("pop from empty stack")
        value = self.main_stack.pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value

    def get_min(self):
        if self.min_stack.is_empty():
            raise ValueError("stack is empty")
        return self.min_stack.peek()

    def is_empty(self):
        return self.main_stack.is_empty()

    def __len__(self):
        return len(self.main_stack)



pilha = MinStack()
pilha.push(5)
pilha.push(3)
pilha.push(7)
pilha.push(2)
pilha.push(8)

print("Mínimo atual:", pilha.get_min())  
pilha.pop()  
print("Mínimo atual:", pilha.get_min())  
pilha.pop()  
print("Mínimo atual:", pilha.get_min())  
pilha.pop()  
print("Mínimo atual:", pilha.get_min())  
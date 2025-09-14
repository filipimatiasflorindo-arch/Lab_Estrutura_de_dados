
from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()
    pares = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in '([{':
            pilha.push(ch)
        elif ch in ')]}':
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if topo != pares[ch]:
                return False

    return pilha.is_empty()

# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False

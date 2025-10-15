def h_index_linear(citacoes):
    n = len(citacoes)
    for i in range(n):
        if citacoes[i] < i + 1:
            return i
    return n

def h_index_binaria(citacoes):
    n = len(citacoes)
    esquerda, direita = 0, n
    h = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if meio == 0:
            esquerda = meio + 1
            continue
        if citacoes[meio - 1] >= meio:
            h = meio
            esquerda = meio + 1
        else:
            direita = meio - 1
    return h


citacoes = [1,2,0,3,4,5,7,5,2,6,8]
print(h_index_binaria(citacoes))
print(h_index_linear(citacoes))
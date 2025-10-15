def quicksort(arr):
    """
    Função principal que inicia o QuickSort.
    Não exige passar índices, apenas o array.
    """
    _quicksort(arr, 0, len(arr) - 1)  # Chama a função recursiva passando os índices corretos.

def _quicksort(arr, left, right):
    """
    Função recursiva que implementa o QuickSort.
    Divide o array em partes menores ao redor do pivô.
    """
    if left < right:  # Caso base: quando a subarray tem pelo menos 2 elementos.
        pi = partition(arr, left, right)  # Particiona o array e obtém o índice do pivô.
        
        # Chamada recursiva para a subarray à esquerda do pivô.
        _quicksort(arr, left, pi - 1)
        
        # Chamada recursiva para a subarray à direita do pivô.
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    """
    Função de particionamento: organiza o array para o QuickSort.
    Coloca o pivô em sua posição correta e garante:
        elementos <= pivô ficam à esquerda dele
        elementos > pivô ficam à direita dele
    """
    pivot = arr[right]  # Escolhe o último elemento como pivô.
    
    i = left - 1  # Ponteiro para a posição de troca: começa antes da subarray.

    pivot = arr[right]  # Escolhe o último elemento como pivô.
    i = left - 1        # Ponteiro para a posição de troca.

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

   
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1  
    # Percorre todos os elementos do subarray.
        # Se o elemento atual for menor ou igual ao pivô...
            # Avança o ponteiro de troca.
            # Troca o elemento atual com o elemento na posição de troca.
    # Após o loop, coloca o pivô na posição correta (entre os menores e os maiores). 
    # Retorna o índice onde o pivô foi colocado.


nums = [2, 0, 3, 1, 1, 0]
quicksort(nums)
print(nums)


def busca_linear_para_insercao(arr_ordenado, alvo):
    for i in range(len(arr_ordenado)):
     
        if arr_ordenado[i] == alvo:
            return i
       
        elif arr_ordenado[i] > alvo:
            return i        
    return len(arr_ordenado)

def busca_binaria_para_insercao(arr_ordenado, alvo):
    esquerda, direita = 0, len(arr_ordenado) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        # Se o alvo for encontrado, retorna seu índice
        if arr_ordenado[meio] == alvo:
            return meio
        # Se o elemento do meio for menor que o alvo, ignora a metade esquerda
        elif arr_ordenado[meio] < alvo:
            esquerda = meio + 1
        # Se o elemento do meio for maior que o alvo, ignora a metade direita
        else:
            direita = meio - 1
    return esquerda

print(busca_binaria_para_insercao(nums, 10))
print(busca_linear_para_insercao(nums, 2))
print(busca_linear_para_insercao(nums, 0))
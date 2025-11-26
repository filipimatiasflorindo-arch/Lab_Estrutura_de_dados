class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data is not None:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simétrica ("in-order")
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.simetric_traversal(node.left)
        print(node)
        if node.right:
            self.simetric_traversal(node.right)
    
    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA:
    def postorder_traversal(self, node=None):
        """
        Realiza o percurso em Pós-Ordem (Postorder):
        Visita o filho esquerdo, depois o filho direito, e por último a raiz.
        """
        if node is None:
            node = self.root
        
        # Percorre a subárvore esquerda
        if node.left:
            self.postorder_traversal(node.left)
        
        # Percorre a subárvore direita
        if node.right:
            self.postorder_traversal(node.right)
        
        # Visita o nó (raiz da subárvore)
        print(node)
    
    def height(self, node=None):
        """
        Calcula a altura da árvore a partir de um determinado nó (incluindo o próprio nó).
        A altura de um nó é o número de arestas no caminho mais longo do nó até uma folha.
        Uma folha tem altura 0.
        """
        if node is None:
            node = self.root
        
        if node is None:
            return -1 # Ou 0, dependendo da convenção. -1 para árvore vazia.

        # Caso base: nó folha (altura 0)
        if node.left is None and node.right is None:
            return 0
        
        # Altura da subárvore esquerda
        height_left = -1
        if node.left:
            height_left = self.height(node.left)
            
        # Altura da subárvore direita
        height_right = -1
        if node.right:
            height_right = self.height(node.right)

        # A altura do nó atual é 1 + o máximo entre as alturas das subárvores.
        return 1 + max(height_left, height_right)

        

def example_tree():
    # Estrutura da árvore:
    #      'A' (root)
    #    /     \
    #  'B'      'C'
    #          /   \
    #        'D'    'E'
    #                \
    #                 'F' 
    
    tree = BinaryTree()
    n1 = Node('B')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')


    n5.right = n6
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree
    
    # Percurso Simétrico (InOrder): Esquerda, Raiz, Direita -> B A D C E F
    # Percurso Pós Ordem (PostOrder): Esquerda, Direita, Raiz -> B D F E C A

if __name__ == '__main__':
    tree = example_tree()
    
    print("---")
    print("🌳 Estrutura da Árvore:")
    print("      'A'")
    print("    /   \\")
    print("  'B'    'C'")
    print("        /   \\")
    print("      'D'    'E'")
    print("               \\")
    print("                'F'")
    print("---")

    print("\nSimetrico - InOrder (Esquerda -> Raiz -> Direita)")
    tree.simetric_traversal() # Esperado: B A D C E F
    
    print("\nPós Ordem - PostOrder (Esquerda -> Direita -> Raiz)")
    tree.postorder_traversal() # Esperado: B D F E C A

    # Altura da árvore inteira (Altura do nó 'A')
    # Caminho mais longo: A -> C -> E -> F (3 arestas)
    altura_total = tree.height()
    print(f"\nAltura da árvore inteira: {altura_total} (A partir da raiz 'A')")

    # Altura de um nó específico (exemplo: nó 'E')
    # Navegando: A -> C -> E
    no_E = tree.root.right.right 
    # Caminho mais longo a partir de 'E': E -> F (1 aresta)
    altura_E = tree.height(no_E)
    print(f"Altura a partir do nó '{no_E.data}': {altura_E}")
    
    # Altura do nó 'D' (nó folha)
    no_D = tree.root.right.left 
    altura_D = tree.height(no_D)
    print(f"Altura a partir do nó '{no_D.data}' (folha): {altura_D}")
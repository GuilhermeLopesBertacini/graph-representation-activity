from typing import Dict, List

class AdjacencyMatrix:
    """
    Classe que representa um grafo usando Matriz de Adjacência.
    """
    def __init__(self):
        """
        Inicializa um grafo vazio.
        """
        self.vertices = []  # Lista de nomes dos vértices
        self.matrix = []    # Matriz de adjacência

def create_graph():
    """
    Cria um novo grafo representado por matriz de adjacência.
    
    Returns:
        AdjacencyMatrix: Grafo vazio
    """
    return AdjacencyMatrix()

def initialize_vertice(graph: AdjacencyMatrix, vertice: str):
    """
    Inicializa (adiciona) um vértice no grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        vertice: Nome do vértice a ser inicializado
    """
    if vertice in graph.vertices:
        return
    
    # Adiciona o vértice à lista
    graph.vertices.append(vertice)
    n = len(graph.vertices)
    
    # Adiciona nova coluna em todas as linhas existentes
    for row in graph.matrix:
        row.append(0)
    
    # Adiciona nova linha para o novo vértice
    graph.matrix.append([0] * n)

def add_edge(graph: AdjacencyMatrix, src: str, dest: str, targeted: bool = False):
    """
    Adiciona uma aresta ao grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, cria aresta direcionada; se False, cria aresta bidirecional
    """
    # Garante que os vértices existem
    initialize_vertice(graph, src)
    initialize_vertice(graph, dest)
    
    # Obtém os índices dos vértices
    src_idx = graph.vertices.index(src)
    dest_idx = graph.vertices.index(dest)
    
    # Adiciona a aresta
    graph.matrix[src_idx][dest_idx] = 1
    if not targeted:
        graph.matrix[dest_idx][src_idx] = 1

def remove_edge(graph: AdjacencyMatrix, src: str, dest: str, targeted: bool = False):
    """
    Remove uma aresta do grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, remove apenas aresta direcionada; se False, remove aresta bidirecional
    """
    if src not in graph.vertices or dest not in graph.vertices:
        return
    
    src_idx = graph.vertices.index(src)
    dest_idx = graph.vertices.index(dest)
    
    graph.matrix[src_idx][dest_idx] = 0
    if not targeted:
        graph.matrix[dest_idx][src_idx] = 0

def remove_vertice(graph: AdjacencyMatrix, vertice: str):
    """
    Remove um vértice do grafo e todas as arestas conectadas a ele.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        vertice: Nome do vértice a ser removido
    """
    if vertice not in graph.vertices:
        return
    
    idx = graph.vertices.index(vertice)
    
    # Remove o vértice da lista
    graph.vertices.pop(idx)
    
    # Remove a linha correspondente
    graph.matrix.pop(idx)
    
    # Remove a coluna correspondente de todas as linhas
    for row in graph.matrix:
        row.pop(idx)

def calculate_vertice_degree(graph: AdjacencyMatrix, vertice: str, targeted: bool = False):
    """
    Calcula o grau de um vértice.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        vertice: Nome do vértice
        targeted: Se True, retorna (grau_entrada, grau_saída); se False, retorna grau total
    
    Returns:
        int ou tuple: Grau do vértice ou tupla (grau_entrada, grau_saída)
    """
    if vertice not in graph.vertices:
        return 0 if not targeted else (0, 0)
    
    idx = graph.vertices.index(vertice)
    
    # Grau de saída: soma da linha
    out_degree = sum(graph.matrix[idx])
    
    if not targeted:
        # Para grafo não direcionado, retorna apenas o grau
        return out_degree
    
    # Grau de entrada: soma da coluna
    in_degree = sum(graph.matrix[i][idx] for i in range(len(graph.vertices)))
    
    return in_degree, out_degree

def check_edge_exists(graph: AdjacencyMatrix, src: str, dest: str) -> bool:
    """
    Verifica se existe uma aresta entre dois vértices.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        src: Vértice de origem
        dest: Vértice de destino
    
    Returns:
        bool: True se a aresta existe, False caso contrário
    """
    if src not in graph.vertices or dest not in graph.vertices:
        return False
    
    src_idx = graph.vertices.index(src)
    dest_idx = graph.vertices.index(dest)
    
    return graph.matrix[src_idx][dest_idx] == 1

def list_neighbors(graph: AdjacencyMatrix, vertice: str) -> List[str]:
    """
    Lista todos os vizinhos (vértices adjacentes) de um vértice.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        vertice: Nome do vértice
    
    Returns:
        list: Lista de vértices vizinhos
    """
    if vertice not in graph.vertices:
        return []
    
    idx = graph.vertices.index(vertice)
    neighbors = []
    
    for i, value in enumerate(graph.matrix[idx]):
        if value == 1:
            neighbors.append(graph.vertices[i])
    
    return neighbors

def check_route_dfs(graph: AdjacencyMatrix, src: str, dest: str) -> bool:
    """
    Verifica se existe um caminho entre dois vértices usando DFS (Busca em Profundidade).
    
    Args:
        graph: Grafo representado por matriz de adjacência
        src: Vértice de origem
        dest: Vértice de destino
    
    Returns:
        bool: True se existe um caminho, False caso contrário
    """
    if src not in graph.vertices or dest not in graph.vertices:
        return False
    
    stack = [src]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == dest:
            return True
        
        # Adiciona vizinhos não visitados à pilha
        neighbors = list_neighbors(graph, node)
        stack.extend(neighbors)
    
    return False

def display_all_degrees(graph: AdjacencyMatrix, targeted: bool = False):
    """
    Exibe o grau de todos os vértices do grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
        targeted: Se True, exibe graus de entrada e saída; se False, exibe grau total
    """
    print("\n=== Graus dos Vértices ===")
    if not graph.vertices:
        print("Grafo vazio!")
        return
    
    for vertice in sorted(graph.vertices):
        degree = calculate_vertice_degree(graph, vertice, targeted)
        if targeted:
            in_deg, out_deg = degree
            print(f"Vértice '{vertice}': Grau de entrada = {in_deg}, Grau de saída = {out_deg}")
        else:
            print(f"Vértice '{vertice}': Grau = {degree}")
    print()

def display_graph(graph: AdjacencyMatrix):
    """
    Exibe a representação visual do grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
    """
    print("\n=== Estrutura do Grafo ===")
    if not graph.vertices:
        print("Grafo vazio!")
        return
    
    for vertice in sorted(graph.vertices):
        neighbors = list_neighbors(graph, vertice)
        if neighbors:
            print(f"{vertice} -> {', '.join(neighbors)}")
        else:
            print(f"{vertice} -> (sem vizinhos)")
    print()

def display_matrix(graph: AdjacencyMatrix):
    """
    Exibe a matriz de adjacência do grafo.
    
    Args:
        graph: Grafo representado por matriz de adjacência
    """
    print("\n=== Matriz de Adjacência ===")
    if not graph.vertices:
        print("Grafo vazio!")
        return
    
    # Cabeçalho
    print("    ", end="")
    for v in graph.vertices:
        print(f"{v:>3}", end="")
    print()
    
    # Linhas da matriz
    for i, v in enumerate(graph.vertices):
        print(f"{v:>3} ", end="")
        for j in range(len(graph.vertices)):
            print(f"{graph.matrix[i][j]:>3}", end="")
        print()
    print()

def main():
    """
    Função principal que demonstra todas as funcionalidades do grafo.
    """
    graph = create_graph()
    
    print("\n2. Inserindo vértices e arestas...")
    add_edge(graph, "A", "B")
    add_edge(graph, "A", "C")
    add_edge(graph, "B", "D")
    add_edge(graph, "C", "D")
    add_edge(graph, "D", "E")
    add_edge(graph, "E", "F")
    initialize_vertice(graph, "G")
    
    display_graph(graph)
    display_matrix(graph)
    
    print("3. Calculando e exibindo graus dos vértices...")
    display_all_degrees(graph)
    
    print("4. Verificando existência de arestas:")
    print(f"   Existe aresta A -> B? {check_edge_exists(graph, 'A', 'B')}")
    print(f"   Existe aresta A -> E? {check_edge_exists(graph, 'A', 'E')}")
    print(f"   Existe aresta G -> A? {check_edge_exists(graph, 'G', 'A')}")
    
    print("\n5. Listando vizinhos:")
    print(f"   Vizinhos de A: {list_neighbors(graph, 'A')}")
    print(f"   Vizinhos de D: {list_neighbors(graph, 'D')}")
    print(f"   Vizinhos de G: {list_neighbors(graph, 'G')}")
    
    print("\n6. Verificando percursos possíveis:")
    print(f"   É possível ir de A até F? {check_route_dfs(graph, 'A', 'F')}")
    print(f"   É possível ir de G até A? {check_route_dfs(graph, 'G', 'A')}")
    print(f"   É possível ir de F até A? {check_route_dfs(graph, 'F', 'A')}")
    
    print("\n7. Removendo aresta D -> E...")
    remove_edge(graph, "D", "E")
    display_graph(graph)
    display_matrix(graph)
    print(f"   É possível ir de A até F agora? {check_route_dfs(graph, 'A', 'F')}")
    
    print("\n8. Removendo vértice C...")
    remove_vertice(graph, "C")
    display_graph(graph)
    display_matrix(graph)
    display_all_degrees(graph)
    
    print("\n9. Testando com grafo direcionado:")
    directed_graph = create_graph()
    add_edge(directed_graph, "X", "Y", targeted=True)
    add_edge(directed_graph, "Y", "Z", targeted=True)
    add_edge(directed_graph, "Z", "X", targeted=True)
    
    display_graph(directed_graph)
    display_matrix(directed_graph)
    display_all_degrees(directed_graph, targeted=True)
    
if __name__ == "__main__":
    main()



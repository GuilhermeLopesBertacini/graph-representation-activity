from typing import List

class EdgeList:
    """
    Classe que representa um grafo usando Lista de Arestas.
    """
    def __init__(self):
        """
        Inicializa um grafo vazio.
        """
        self.vertices = set()  # Conjunto de vértices
        self.edges = []        # Lista de arestas (tuplas)

def create_graph():
    """
    Cria um novo grafo representado por lista de arestas.
    
    Returns:
        EdgeList: Grafo vazio
    """
    return EdgeList()

def initialize_vertice(graph: EdgeList, vertice: str):
    """
    Inicializa um vértice no grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
        vertice: Nome do vértice a ser inicializado
    """
    graph.vertices.add(vertice)

def add_edge(graph: EdgeList, src: str, dest: str, targeted: bool = False):
    """
    Adiciona uma aresta ao grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, cria aresta direcionada; se False, cria aresta bidirecional
    """
    # Garante que os vértices existem
    initialize_vertice(graph, src)
    initialize_vertice(graph, dest)
    
    # Verifica se a aresta já existe
    if (src, dest) not in graph.edges:
        graph.edges.append((src, dest))
    
    # Se não for direcionado, adiciona aresta inversa
    if not targeted and (dest, src) not in graph.edges:
        graph.edges.append((dest, src))

def remove_edge(graph: EdgeList, src: str, dest: str, targeted: bool = False):
    """
    Remove uma aresta do grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, remove apenas aresta direcionada; se False, remove aresta bidirecional
    """
    # Remove a aresta (src, dest)
    if (src, dest) in graph.edges:
        graph.edges.remove((src, dest))
    
    # Se não for direcionado, remove aresta inversa
    if not targeted and (dest, src) in graph.edges:
        graph.edges.remove((dest, src))

def remove_vertice(graph: EdgeList, vertice: str):
    """
    Remove um vértice do grafo e todas as arestas conectadas a ele.
    
    Args:
        graph: Grafo representado por lista de arestas
        vertice: Nome do vértice a ser removido
    """
    if vertice not in graph.vertices:
        return
    
    # Remove o vértice do conjunto
    graph.vertices.remove(vertice)
    
    # Remove todas as arestas que contêm o vértice
    graph.edges = [(src, dest) for src, dest in graph.edges 
                   if src != vertice and dest != vertice]

def calculate_vertice_degree(graph: EdgeList, vertice: str, targeted: bool = False):
    """
    Calcula o grau de um vértice.
    
    Args:
        graph: Grafo representado por lista de arestas
        vertice: Nome do vértice
        targeted: Se True, retorna (grau_entrada, grau_saída); se False, retorna grau total
    
    Returns:
        int ou tuple: Grau do vértice ou tupla (grau_entrada, grau_saída)
    """
    if vertice not in graph.vertices:
        return 0 if not targeted else (0, 0)
    
    # Conta grau de saída (arestas que saem do vértice)
    out_degree = sum(1 for src, dest in graph.edges if src == vertice)
    
    if not targeted:
        # Para grafo não direcionado, o grau já está contado corretamente
        return out_degree
    
    # Conta grau de entrada (arestas que chegam no vértice)
    in_degree = sum(1 for src, dest in graph.edges if dest == vertice)
    
    return in_degree, out_degree

def check_edge_exists(graph: EdgeList, src: str, dest: str) -> bool:
    """
    Verifica se existe uma aresta entre dois vértices.
    
    Args:
        graph: Grafo representado por lista de arestas
        src: Vértice de origem
        dest: Vértice de destino
    
    Returns:
        bool: True se a aresta existe, False caso contrário
    """
    return (src, dest) in graph.edges

def list_neighbors(graph: EdgeList, vertice: str) -> List[str]:
    """
    Lista todos os vizinhos (vértices adjacentes) de um vértice.
    
    Args:
        graph: Grafo representado por lista de arestas
        vertice: Nome do vértice
    
    Returns:
        list: Lista de vértices vizinhos
    """
    if vertice not in graph.vertices:
        return []
    
    neighbors = []
    for src, dest in graph.edges:
        if src == vertice:
            neighbors.append(dest)
    
    return neighbors

def check_route_dfs(graph: EdgeList, src: str, dest: str) -> bool:
    """
    Verifica se existe um caminho entre dois vértices usando DFS (Busca em Profundidade).
    
    Args:
        graph: Grafo representado por lista de arestas
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

def display_all_degrees(graph: EdgeList, targeted: bool = False):
    """
    Exibe o grau de todos os vértices do grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
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

def display_graph(graph: EdgeList):
    """
    Exibe a representação visual do grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
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

def display_edges(graph: EdgeList):
    """
    Exibe a lista de arestas do grafo.
    
    Args:
        graph: Grafo representado por lista de arestas
    """
    print("\n=== Lista de Arestas ===")
    if not graph.edges:
        print("Nenhuma aresta no grafo!")
        return
    
    print(f"Total de arestas: {len(graph.edges)}")
    for i, (src, dest) in enumerate(graph.edges, 1):
        print(f"{i}. {src} -> {dest}")
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
    display_edges(graph)
    
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
    display_edges(graph)
    print(f"   É possível ir de A até F agora? {check_route_dfs(graph, 'A', 'F')}")
    
    print("\n8. Removendo vértice C...")
    remove_vertice(graph, "C")
    display_graph(graph)
    display_edges(graph)
    display_all_degrees(graph)
    
    print("\n9. Testando com grafo direcionado:")
    directed_graph = create_graph()
    add_edge(directed_graph, "X", "Y", targeted=True)
    add_edge(directed_graph, "Y", "Z", targeted=True)
    add_edge(directed_graph, "Z", "X", targeted=True)
    
    display_graph(directed_graph)
    display_edges(directed_graph)
    display_all_degrees(directed_graph, targeted=True)

if __name__ == "__main__":
    main()

from collections import defaultdict
from typing import Dict

def create_graph():
    """
    Cria um novo grafo representado por lista de adjacência.
    
    Returns:
        defaultdict: Grafo vazio
    """
    graph = defaultdict(list)
    return graph

def initialize_vertice(graph: Dict, vertice: str):
    """
    Inicializa um vértice no grafo.
    
    Args:
        graph: Grafo representado por lista de adjacência
        vertice: Nome do vértice a ser inicializado
    """
    if vertice in graph:
        return
    graph[vertice] = []

def add_edge(graph: Dict, src: str, dest: str, targeted: bool = False):
    """
    Adiciona uma aresta ao grafo.
    
    Args:
        graph: Grafo representado por lista de adjacência
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, cria aresta direcionada; se False, cria aresta bidirecional
    """
    initialize_vertice(graph, src)
    initialize_vertice(graph, dest)
    
    graph[src].append(dest)
    if not targeted:
        graph[dest].append(src)

def remove_edge(graph: Dict, src: str, dest: str, targeted: bool = False):
    """
    Remove uma aresta do grafo.
    
    Args:
        graph: Grafo representado por lista de adjacência
        src: Vértice de origem
        dest: Vértice de destino
        targeted: Se True, remove apenas aresta direcionada; se False, remove aresta bidirecional
    """
    try:
        if src in graph:
            graph[src].remove(dest)
        if not targeted:
            if dest in graph:
                graph[dest].remove(src)
    except ValueError:
        pass

def remove_vertice(graph: Dict, vertice: str):
    """
    Remove um vértice do grafo e todas as arestas conectadas a ele.
    
    Args:
        graph: Grafo representado por lista de adjacência
        vertice: Nome do vértice a ser removido
    """
    if vertice in graph:
        del graph[vertice]
    
    for v in list(graph.keys()):
        graph[v] = [neighbor for neighbor in graph[v] if neighbor != vertice]

def calculate_vertice_degree(graph: Dict, vertice: str, targeted: bool = False):
    """
    Calcula o grau de um vértice.
    
    Args:
        graph: Grafo representado por lista de adjacência
        vertice: Nome do vértice
        targeted: Se True, retorna (grau_entrada, grau_saída); se False, retorna grau total
    
    Returns:
        int ou tuple: Grau do vértice ou tupla (grau_entrada, grau_saída)
    """
    if vertice not in graph:
        return 0 if not targeted else (0, 0)

    out_degree = len(graph[vertice])
    if not targeted:
        return out_degree
    
    in_degree = 0
    for v in graph.keys():
        in_degree += graph[v].count(vertice)
        
    return in_degree, out_degree

def check_edge_exists(graph: dict, src: str, dest: str) -> bool:
    """
    Verifica se existe uma aresta entre dois vértices.
    
    Args:
        graph: Grafo representado por lista de adjacência
        src: Vértice de origem
        dest: Vértice de destino
    
    Returns:
        bool: True se a aresta existe, False caso contrário
    """
    if src not in graph:
        return False
    return dest in graph[src]

def list_neighbors(graph: dict, vertice: str):
    """
    Lista todos os vizinhos (vértices adjacentes) de um vértice.
    
    Args:
        graph: Grafo representado por lista de adjacência
        vertice: Nome do vértice
    
    Returns:
        list: Lista de vértices vizinhos
    """
    # Em caso de Key Error, default dict retornará uma lista vazia
    return graph[vertice]

def check_route_dfs(graph: dict, src: str, dest: str) -> bool:
    """
    Verifica se existe um caminho entre dois vértices usando DFS (Busca em Profundidade).
    
    Args:
        graph: Grafo representado por lista de adjacência
        src: Vértice de origem
        dest: Vértice de destino
    
    Returns:
        bool: True se existe um caminho, False caso contrário
    """
    if src not in graph or dest not in graph:
        return False
    
    stack = []
    stack.append(src)
    visited = set()
    while len(stack) != 0:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == dest:
            return True
        stack.extend(graph[node])
    return False

def display_all_degrees(graph: dict, targeted: bool = False):
    """
    Exibe o grau de todos os vértices do grafo.
    
    Args:
        graph: Grafo representado por lista de adjacência
        targeted: Se True, exibe graus de entrada e saída; se False, exibe grau total
    """
    print("\n=== Graus dos Vértices ===")
    if not graph:
        print("Grafo vazio!")
        return
    
    for vertice in sorted(graph.keys()):
        degree = calculate_vertice_degree(graph, vertice, targeted)
        if targeted:
            in_deg, out_deg = degree
            print(f"Vértice '{vertice}': Grau de entrada = {in_deg}, Grau de saída = {out_deg}")
        else:
            print(f"Vértice '{vertice}': Grau = {degree}")
    print()

def display_graph(graph: dict):
    """
    Exibe a representação visual do grafo.
    
    Args:
        graph: Grafo representado por lista de adjacência
    """
    print("\n=== Estrutura do Grafo ===")
    if not graph:
        print("Grafo vazio!")
        return
    
    for vertice in sorted(graph.keys()):
        neighbors = graph[vertice]
        if neighbors:
            print(f"{vertice} -> {', '.join(neighbors)}")
        else:
            print(f"{vertice} -> (sem vizinhos)")
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
    print(f"   É possível ir de A até F agora? {check_route_dfs(graph, 'A', 'F')}")
    
    print("\n8. Removendo vértice C...")
    remove_vertice(graph, "C")
    display_graph(graph)
    display_all_degrees(graph)
    
    print("\n9. Testando com grafo direcionado:")
    directed_graph = create_graph()
    add_edge(directed_graph, "X", "Y", targeted=True)
    add_edge(directed_graph, "Y", "Z", targeted=True)
    add_edge(directed_graph, "Z", "X", targeted=True)
    
    display_graph(directed_graph)
    display_all_degrees(directed_graph, targeted=True)
    
if __name__ == "__main__":
    main()



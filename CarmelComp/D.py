from collections import defaultdict, deque

def inputToGraph():
    vertices, edges = map(int, input().split())
    adjacency_list = {i: [] for i in range(vertices)}

    for _ in range(edges):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list, vertices

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    component = []

    while queue:
        node = queue.popleft()
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return component

def find_connected_components(graph, n):
    visited = [False] * n
    components = []      

    for node in range(n):
        if not visited[node]:
            component = bfs(graph, visited, node)
            components.append(component)

    return components

def is_cyclic_component(graph, component):
    edges = 0
    for node in component:
        edges += len(graph[node])
        if len(graph[node]) != 2:
            return False

    edges //= 2
    return edges == len(component)

def count_cyclic_components(graph, n):
    components = find_connected_components(graph, n)
    cyclic_count = 0

    for component in components:  
        if is_cyclic_component(graph, component): 
            cyclic_count += 1

    return cyclic_count

def main():
    graph, n = inputToGraph()
    print("result:", count_cyclic_components(graph, n))

if __name__ == "__main__":
    main()
# אם יש מעגל אי זוגי אז 0
# גרף הוא דו-צדדי אם ורק אם אין בו מעגל באורך אי-זוגי

from collections import deque

def isBipartite(graph):
    # `graph` is an adjacency list representation: {0: [1, 2], 1: [0, 3], ...}
    n = len(graph)  # Number of vertices
    side = [-1] * n  # -1 means unvisited, 0 and 1 are sides for bipartite check
    sizeOfGroups = [1,0]

    for start in range(n):  # Handle disconnected graphs
        if side[start] == -1:  # Unvisited node
            queue = deque([start])
            side[start] = 0  # Start sideing with 0

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    if side[v] == -1:  # If unvisited, side it with the opposite side
                        side[v] = 1 - side[u]
                        sizeOfGroups[side[v]] += 1
                        queue.append(v)
                    elif side[v] == side[u]:  # Found two vertices with the same side
                        return False, None  # Odd cycle detected

    return True, sizeOfGroups  # No odd-length cycle found

def calcNumOfNiceGraphs(size1, size2):
    res = (2 ** size1 + 2 ** size2) % 998244353
    print(res)

def inputToGraph():
    # Read the number of vertices and edges
    vertices, edges = map(int, input().split())

    # Initialize an empty adjacency list
    adjacency_list = {i: [] for i in range(vertices)}

    # Read the edges
    for _ in range(edges):
        u, v = map(int, input().split())
        # Convert to 0-based indexing for consistency
        u -= 1
        v -= 1
        # Add the edge to the adjacency list
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list

    

def main():
    t = input()
    graph = inputToGraph()
    print(graph)
    isB, sizes = isBipartite(graph)
    if (isB):
        calcNumOfNiceGraphs(sizes[0], sizes[1])
    else:
        print('0')

if __name__ == "__main__":
    main()
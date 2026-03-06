print("Part 1: BFS without Queue and without Node")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_simple(graph, start):
    visited = []
    queue = [start]
    visited.append(start)

    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs_simple(graph, 'A')


print("\n\nPart 2: BFS with Queue and Node")

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

def bfs_with_node(graph, start):
    visited = set()
    q = deque()
    q.append(Node(start))
    visited.add(start)

    while q:
        current = q.popleft()
        print(current.value, end=" ")
        for neighbour in graph[current.value]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(Node(neighbour))

bfs_with_node(graph, 'A')
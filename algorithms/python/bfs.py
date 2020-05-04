from collections import defaultdict

class Graph:
    #constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # Mark all vertices as not visited
        visited = [False] * len(self.graph)

        # Create a queue for BFS
        queue = []

        # Mark the source as visited and enqueue
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex and print
            s = queue.pop(0)
            print(s, end = " ")

            # Queue all adjactent Vertices of s if not visited
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code

# Create a graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Starting BFS from 2")

g.BFS(2)
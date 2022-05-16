# Assignment 1
#
# Implement depth first search algorithm and Breadth First Search algorithm,
# Use an undirected graph and develop a recursive algorithm for searching
# all the vertices of a graph or tree data structure.


class Graph:
    def __init__(self, adj=None):
        self.input_dimensions()
        self.adj = [[] for _ in range(self.v)]
        self.input_graph()

    def input_dimensions(self):
        self.v = int(input("Enter number of vertices here: "))
        self.e = int(input("Enter number of edges here: "))
        print()

    def input_graph(self):
        print("!! Caution: zero-indexed !!")
        for i in range(self.e):
            src = int(input(f"Enter starting point for edge {str(i)}: "))
            dest = int(input(f"Enter ending point for edge {str(i)}: "))
            self.adj[src].append(dest)
            self.adj[dest].append(src)
            print()

    def print(self):
        for i in range(self.v):
            print(i, end=" ")
            print(self.adj[i])

    def _bfs(self, queue, visited):
        if len(queue) == 0:
            return

        start = queue.pop(0)
        print(start, end=" ")
        visited[start] = True
        for elem in self.adj[start]:
            if visited[elem] == False:
                visited[elem] = True
                queue.append(elem)

        self._bfs(queue, visited)

    def bfs(self, start):
        visited = [False] * self.v
        queue = [start]
        self._bfs(queue, visited)

    def _dfs(self, queue, visited):
        if len(queue) == 0:
            return

        start = queue.pop(0)
        print(start, end=" ")
        visited[start] = True
        for elem in self.adj[start]:
            if visited[elem] == False:
                visited[elem] = True
                queue.append(elem)

                self._dfs(queue, visited)

    def dfs(self, start):
        visited = [False] * self.v
        queue = [start]
        self._dfs(queue, visited)


def menu():
    flag = True
    while (flag):
        g = Graph()
        g.print()
        start = int(input("BFS : Enter the vertex to start: "))
        g.bfs(start)
        print()
        start = int(input("DFS : Enter the vertex to start: "))
        g.dfs(start)
        print()
        print("Do you want to continue?(y/n)")
        cont = input().lower()
        if (cont.startswith("n")):
            flag = False


menu()
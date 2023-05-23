import array as arr
import numpy as np
from collections import defaultdict

class funck_graph:

    def __init__(self, vertex, direcred=False):
        self.graph = defaultdict(list)
        self.V = vertex
        self.directed = direcred

    def go_weight(self, number, weight):
        self.graph[number].append(weight)
        if self.directed is False:
            self.graph[weight].append(number)
        else:
            self.graph[weight] = self.graph[weight]

    def Tarjan(self):
        visited_list = {i: False for i in self.graph}
        sorted_list = []

        for v in self.graph:
            if not visited_list[v]:
                self.go_in_Node(v, visited_list, sorted_list)

        print(sorted_list)

    def go_in_Node(self, number, visited_list, sorted_list):
        visited_list[number] = True
        for i in self.graph[number]:
            if not visited_list[i]:
                self.go_in_Node(i, visited_list, sorted_list)
        sorted_list.insert(0, number)

class fler:

    def __init__(self, vertex, direcred=False):
        self.graph = defaultdict(list)
        self.V = vertex
        self.directed = direcred


    def printEulerUtil(self, u):

        for v in self.graph[u]:

            if self.isValidNextEdge(u, v):
                print("%d-%d " % (u, v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)

    def isValidNextEdge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        else:

            visited = [False] * (self.V)
            count1 = self.DFSCount(u, visited)

            self.rmvEdge(u, v)
            visited = [False] * (self.V)
            count2 = self.DFSCount(u, visited)

            self.addEdge(u, v)

            return False if count1 > count2 else True

    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

    def addEdge(self, frm, to):
        self.graph[frm].append(to)
        if self.directed is False:
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    def printEulerTour(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        self.printEulerUtil(u)


class euler:

    def find_eulerian_tour(graph):
        stack = [];
        tour = []

        stack.append(graph[0][0])

        while len(stack) > 0:
            v = stack[len(stack) - 1]

            degree = euler.get_degree(v, graph)

            if degree == 0:
                stack.pop()
                tour.append(v)
            else:
                index, edge = euler.get_edge_and_index(v, graph)
                graph.pop(index)
                stack.append(edge[1] if v == edge[0] else edge[0])
        return tour

    def get_degree(v, graph):
        degree = 0
        for (x, y) in graph:
            if v == x or v == y:
                degree += 1

        return degree

    def get_edge_and_index(v, graph):
        edge = ();
        index = -1

        for i in range(len(graph)):
            if (v == graph[i][0] or v == graph[i][1]):
                edge, index = graph[i], i
                break

        return index, edge


class kosaryju:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def addEdge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = kosaryju(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")
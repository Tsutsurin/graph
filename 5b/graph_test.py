import graph_b
import networkx as nx
import matplotlib.pyplot as plt

graph = graph_b.funck_graph(6, direcred=True)

graph.go_weight(1, 6)
graph.go_weight(1, 3)
graph.go_weight(2, 1)
graph.go_weight(2, 5)
graph.go_weight(3, 4)
graph.go_weight(5, 1)
graph.go_weight(5, 6)
graph.go_weight(6, 3)
graph.go_weight(6, 4)
print("\nАлгоритм Тарьяна: \n")
graph.Tarjan()


graph1 = graph_b.fler(6, direcred=True)

graph1.addEdge(1, 6)
graph1.addEdge(1, 3)
graph1.addEdge(2, 1)
graph1.addEdge(2, 5)
graph1.addEdge(3, 4)
graph1.addEdge(5, 1)
graph1.addEdge(5, 6)
graph1.addEdge(6, 3)
graph1.addEdge(6, 4)
print("\nАлгоритм Флёри \n")
graph1.printEulerTour()


graph2 = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print("\nАлгоритм поиска элерова цикла \n")
print((graph_b.euler.find_eulerian_tour(graph2)))


graph3 = graph_b.kosaryju(5)
graph3.addEdge(1, 0)
graph3.addEdge(0, 2)
graph3.addEdge(2, 1)
graph3.addEdge(0, 3)
graph3.addEdge(3, 4)

print("\nАлгоритм Косарайю \n")
graph3.print_scc()
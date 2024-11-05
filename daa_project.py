import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


city_graph = nx.Graph()
city_graph.add_weighted_edges_from([
    ("A", "B", 5), ("A", "C", 2), ("B", "C", 8), ("B", "D", 7),
    ("C", "D", 1), ("C", "E", 3), ("D", "E", 2), ("D", "F", 4),
    ("E", "F", 6)
])


pos = nx.spring_layout(city_graph)
nx.draw(city_graph, pos, with_labels=True, node_color="skyblue", node_size=700)
edge_labels = nx.get_edge_attributes(city_graph, 'weight')
nx.draw_networkx_edge_labels(city_graph, pos, edge_labels=edge_labels)
plt.show()


def dijkstra_shortest_path(graph, start, end):
    path = nx.dijkstra_path(graph, start, end, weight='weight')
    length = nx.dijkstra_path_length(graph, start, end, weight='weight')
    return path, length

path, length = dijkstra_shortest_path(city_graph, 'A', 'F')
print("Dijkstra's Shortest Path:", path)
print("Path Length:", length)


def euclidean_heuristic(u, v, pos):
    (x1, y1) = pos[u]
    (x2, y2) = pos[v]
    return np.sqrt((x1 - x2) * 2 + (y1 - y2) * 2)


pos = {
    "A": (0, 0), "B": (5, 0), "C": (3, 2),
    "D": (7, 2), "E": (4, 4), "F": (6, 5)
}


def astar_path(graph, start, end, heuristic):
    path = nx.astar_path(graph, start, end, heuristic=lambda u, v: heuristic(u, v, pos), weight='weight')
    length = nx.astar_path_length(graph, start, end, heuristic=lambda u, v: heuristic(u, v, pos), weight='weight')
    return path, length


path, length = astar_path(city_graph, 'A', 'F', euclidean_heuristic)
print("A* Shortest Path:", path)
print("Path Length:", length)

dijkstra_path, dijkstra_length = dijkstra_shortest_path(city_graph, 'A', 'F')
astar_path, astar_length = astar_path(city_graph, 'A', 'F', euclidean_heuristic)
print("\nComparison of Algorithms:")
print("Dijkstra's Path:", dijkstra_path, "Length:", dijkstra_length)
print("A* Path:", astar_path, "Length:", astar_length)


def visualize_path(graph, path, pos, title="Path Visualization"):
    plt.figure()
    nx.draw(graph, pos, with_labels=True, node_color="lightgreen", node_size=700)
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)],
                           edge_color="orange", width=2)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

visualize_path(city_graph, dijkstra_path, pos, title="Dijkstra's Path from A to F")


visualize_path(city_graph, astar_path, pos, title="A* Path from A to F")

from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    already_visited = []
    shortest_path = dict()
    general = [starting_node] + [p for p in g.nodes if p != starting_node]

    for given_node in g.nodes:
        if given_node != starting_node:
            shortest_path[given_node] = float("inf")
        else:
            shortest_path[given_node] = 0

    current_node = starting_node

    while general:

        sorted_min = [(i, g.get_edge_data(current_node, i)["weight"]) for i in g.neighbors(current_node)]
        sorted_min.sort(key=lambda x: x[1])
        to_visit = [j[0] for j in sorted_min if j[0] not in already_visited]

        for node in to_visit:
            if node not in already_visited:
                weight_to_check = g.get_edge_data(current_node, node)["weight"] + shortest_path[current_node]
                current_weight = shortest_path[node]
                if weight_to_check < current_weight:
                    shortest_path[node] = weight_to_check

        already_visited.append(current_node)
        general.remove(current_node)

        if to_visit:
            current_node = to_visit.pop(0)
        else:
            if general:
                current_node = general[0]

    return shortest_path


if __name__ == '__main__':
    G = nx.Graph()
    G.add_nodes_from("123456")
    G.add_weighted_edges_from([
        ("1", "2", 7),
        ("1", "3", 9),
        ("1", "6", 14),
        ("6", "3", 2),
        ("3", "4", 11),
        ("2", "4", 15),
        ("2", "3", 10),
        ("5", "4", 6),
        ("6", "5", 9),
        ("5", "4", 6),
    ])
    print(dijkstra_algo(G, '1'))

    P = nx.DiGraph()
    P.add_nodes_from("ABCDEFGH")
    P.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
        ("H", "D", 1),
        ("D", "G", 2),
        ("G", "H", 1),
    ])
    print(dijkstra_algo(P, 'D'))

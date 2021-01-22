from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    stack_to_visit = [start_node]
    already_visited = []

    while stack_to_visit:
        current_node = stack_to_visit.pop(-1)
        already_visited.append(current_node)

        for node in g.neighbors(current_node):
            if node not in already_visited and node not in stack_to_visit:
                stack_to_visit.append(node)

    return already_visited


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
        ('G', 'D'),
        ('G', 'F'),
    ])
    print(dfs(graph, 'A'))

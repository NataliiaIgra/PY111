from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    already_visited = [start_node]
    queue_to_visit = [start_node]

    while queue_to_visit:
        current_node = queue_to_visit.pop(0)

        for node in g.neighbors(current_node):
            if node not in already_visited:
                queue_to_visit.append(node)
                already_visited.append(node)

    return already_visited

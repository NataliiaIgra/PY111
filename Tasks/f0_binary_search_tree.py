"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx
import matplotlib.pyplot as plt

Tree = nx.DiGraph()
root = None

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global Tree, root
    if not Tree.nodes:
        Tree.add_node(key, data=value)
        root = key
    else:
        current_node = root
        search = True
        while search:
            if key == current_node:
                Tree.nodes[key]['data'] = value
                search = False
            else:
                neighbours = list(Tree.neighbors(current_node))
                if not neighbours:
                    Tree.add_node(key, data=value)
                    Tree.add_edge(current_node, key)
                    search = False
                elif len(neighbours) == 1:
                    if neighbours[0] > current_node:
                        if key > current_node:
                            current_node = neighbours[0]
                        else:
                            Tree.add_node(key, data=value)
                            Tree.add_edge(current_node, key)
                            search = False
                    else:
                        if key > current_node:
                            Tree.add_node(key, data=value)
                            Tree.add_edge(current_node, key)
                            search = False
                        else:
                            current_node = neighbours[0]
                else:
                    if key > current_node:
                        current_node = max(neighbours)
                    else:
                        current_node = min(neighbours)
    return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global Tree, root
    parent_node = root
    current_node = root
    search = True
    while search:
        if key == current_node:
            neighbours = list(Tree.neighbors(current_node))
            if not neighbours:
                Tree.remove_node(current_node)
            search = False

    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global Tree
    exist_nodes = list(Tree.nodes)
    if key in exist_nodes:
        return Tree.nodes[key]['data']
    else:
        raise KeyError


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global Tree, root
    Tree.clear()
    root = None
    return None

if __name__ == '__main__':
    insert(42, 'The meaning of life, the universe and everything.')
    insert(0, 'ZERO!')
    insert(13, "Devil's sign here")
    insert(50, "blabla")
    insert(60, "blabla")
    insert(44, "blabla")
    insert(55, "blabla")
    insert(60, "blabla")
    insert(33, "blabla")
    insert(66, "blabla")
    insert(51, "blabla")
    insert(9, "blabla")
    print(Tree.edges)
    print(Tree.nodes)
    Tree.remove_node(60)
    print(Tree.edges)
    print(Tree.nodes)
    Tree.add_edge(42, 42)
    nx.draw(Tree, with_labels=True)
    plt.show()

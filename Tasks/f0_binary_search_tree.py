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
    found = find_all(key)
    if not found:
        return None
    else:
        neighbours = found[2]
        parent_node = found[0]
        if not neighbours:
            Tree.remove_node(key)
            if key == root:
                root = None
        elif len(neighbours) == 1:
            Tree.remove_node(key)
            if parent_node != None:
                Tree.add_edge(parent_node, neighbours[0])
            else:
                root = neighbours[0]
        else:
            saved_neighbour_min = min(neighbours)
            saved_neighbour_max = max(neighbours)
            current_node = max(neighbours)
            while True:
                neighbours = list(Tree.neighbors(current_node))
                if not neighbours:

                    if current_node != saved_neighbour_max:
                        Tree.remove_node(key)
                        Tree.remove_edge(saved_parent, current_node)
                        Tree.add_edge(current_node, saved_neighbour_max)
                        Tree.add_edge(current_node, saved_neighbour_min)
                        if parent_node == None:
                            root = current_node
                        else:
                            Tree.add_edge(parent_node, current_node)
                        return None

                    elif current_node == saved_neighbour_max:
                        Tree.remove_node(key)
                        if parent_node == None:
                            Tree.add_edge(saved_neighbour_max, saved_neighbour_min)
                            root = saved_neighbour_max
                        else:
                            Tree.add_edge(current_node, saved_neighbour_min)
                            Tree.add_edge(parent_node, current_node)
                        return None

                elif len(neighbours) == 1:
                    if neighbours[0] > current_node:

                        if current_node != saved_neighbour_max:
                            Tree.remove_node(key)
                            Tree.remove_edge(saved_parent, current_node)
                            Tree.remove_edge(current_node, neighbours[0])
                            Tree.add_edge(current_node, saved_neighbour_min)
                            Tree.add_edge(current_node, saved_neighbour_max)
                            Tree.add_edge(saved_parent, neighbours[0])
                            if parent_node == None:
                                root = current_node
                            else:
                                Tree.add_edge(parent_node, current_node)
                            return None

                        if current_node == saved_neighbour_max:
                            Tree.remove_node(key)
                            if parent_node == None:
                                Tree.add_edge(saved_neighbour_max, saved_neighbour_min)
                                root = saved_neighbour_max
                            else:
                                Tree.add_edge(parent_node, current_node)
                                Tree.add_edge(current_node, saved_neighbour_min)
                            return None

                    elif neighbours[0] < current_node:
                        saved_parent = current_node
                        current_node = neighbours[0]
                else:
                    saved_parent = current_node
                    current_node = min(neighbours)


def find_all(given_node):
    global Tree, root
    if not Tree:
        return None
    parent_node = root
    current_node = root
    while True:
        if given_node == root:
            return None, Tree.nodes[current_node]['data'], list(Tree.neighbors(given_node))
        else:
            neighbours = list(Tree.neighbors(current_node))
            if not neighbours and given_node == current_node:
                return parent_node, Tree.nodes[current_node]['data'], list(Tree.neighbors(given_node))
            if not neighbours and given_node != current_node:
                return None
            if len(neighbours) == 1:
                if given_node == current_node:
                    return parent_node, Tree.nodes[current_node]['data'], list(Tree.neighbors(current_node))
                parent_node = current_node
                current_node = neighbours[0]
                if given_node == current_node:
                    return parent_node, Tree.nodes[current_node]['data'], list(Tree.neighbors(current_node))
                else:
                    parent_node = neighbours[0]
            elif len(neighbours) == 2:
                if given_node == current_node:
                    return parent_node, Tree.nodes[current_node]['data'], list(Tree.neighbors(current_node))
                elif given_node > current_node:
                    parent_node = current_node
                    current_node = max(neighbours)
                else:
                    parent_node = current_node
                    current_node = min(neighbours)


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global Tree, root
    found = find_all(key)
    if not found:
        raise KeyError
    else:
        return found[1]


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
    insert(50, 'ZERO!')
    insert(30, 'ZERO!')
    insert(55, 'ZERO!')
    insert(13, "Devil's sign here")
    insert(45, "Crocodile")
    insert(46, "Crocodile")
    insert(47, "Crocodile")
    insert(44, "Crocodile")
    insert(53, "Crocodile")
    insert(56, "Crocodile")
    insert(54, "Crocodile")
    insert(60, "Crocodile")
    insert(54, "Crocodile")
    insert(53, "Crocodile")
    insert(35, "Crocodile")
    insert(32, "pa-pa")
    insert(33, "parapapapa")
    insert(36, "parapapapa")
    insert(31, "vcds")
    remove(30)
    remove(42)
    remove(44)
    remove(55)
    remove(50)
    remove(46)
    remove(35)
    remove(33)
    remove(31)
    remove(53)
    remove(56)
    remove(45)
    remove(60)
    remove(13)
    remove(36)
    remove(47)
    remove(32)
    remove(54)
    print(list(Tree.nodes))
    print(list(Tree.edges))
    print(root)
    nx.draw_planar(Tree, with_labels=True)
    plt.show()



# coding:utf-8
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.prev_node = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.prev_node[v].append(u)

    def get_previous_nodes(self, node):
        return self.prev_node[node]

    def get_next_nodes(self, node):
        return self.graph[node]

    def find_nodes(self, length):
        all_paths = []

        for node in range(length):
            next_nodes = self.get_next_nodes(node)
            prev_nodes = self.get_previous_nodes(node)

            if next_nodes and prev_nodes:
                for prev_node in prev_nodes:
                    for next_node in next_nodes:
                        all_paths.append((prev_node, node, next_node))
            elif next_nodes:
                for next_node in next_nodes:
                    all_paths.append((None, node, next_node))
            elif prev_nodes:
                for prev_node in prev_nodes:
                    all_paths.append((prev_node, node, None))

        return all_paths

    def remove_last_if_equal(self, paths):
        modified_paths = []
        for path in paths:
            if path[0] == path[-1]:
                modified_paths.append(path[:-1] + (None,))
            else:
                modified_paths.append(path)
        return modified_paths


# Read adjacency matrix data from a txt file
def read_adjacency_matrix_from_file(file_path):
    adjacency_matrix = []
    with open(file_path, "r") as file:
        content = file.read()
        # Using the eval method to convert a string into a list
        adjacency_matrix = eval(content)
    return adjacency_matrix

# adj_matrix = [[0, 1, 0, 1, 0, 0, 1],
#               [0, 0, 1, 0, 0, 0, 0],
#               [0, 1, 0, 1, 0, 0, 0],
#               [0, 0, 1, 0, 1, 0, 0],
#               [0, 1, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 1],
#               [0, 0, 0, 0, 0, 0, 0]]

# Call a function to read the adjacency matrix
adj_matrix = read_adjacency_matrix_from_file("./adjacency_matrix.txt")

# Create an empty directed graph object
g = Graph()

# Add edges to the directed graph based on the adjacency matrix
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            g.add_edge(i, j)

nodes = g.find_nodes(len(adj_matrix))
modified_nodes = g.remove_last_if_equal(nodes)

print(modified_nodes)
print("--------------------")


def search(new_node, modified_nodes):
    if new_node is not None:
        if new_node[0] is None:
            current_path = []
            visited_nodes = set()
            not_found = True
            current_node = node[1]
            next_node = node[2]
            visited_nodes.add(current_node)
            visited_nodes.add(next_node)
            current_path.append(current_node)
            current_path.append(next_node)
            for node2 in modified_nodes:
                if (
                    current_node is node2[0]
                    and node2[1] is next_node
                    and node2[2] is None
                ):
                    not_found = False
                    path_list.append(current_path.copy())
                elif (
                    node2[0] is current_node
                    and node2[1] is next_node
                    and node2[2] is not None
                    and node2[2] not in visited_nodes
                ):
                    current_path.append(node2[2])
                    visited_nodes.add(node2[2])
                    current_node = node2[1]
                    next_node = node2[2]
            new_node = None

            if not_found:
                record = tuple(current_path.copy())
                new_node = modified_nodes[modified_nodes.index(record) + 1]

            while not_found:
                path_list.append(current_path.copy())
                for node3 in modified_nodes:
                    if (
                        current_node is node3[0]
                        and node3[1] is next_node
                        and node3[2] is None
                    ):
                        not_found = False
                        if current_path.copy() not in path_list:
                            path_list.append(current_path.copy())
                    elif (
                        node3[0] is current_node
                        and node3[1] is next_node
                        and node3[2] is not None
                        and node3[2] not in visited_nodes
                    ):
                        current_path.append(node3[2])
                        visited_nodes.add(node3[2])
                        current_node = node3[1]
                        next_node = node3[2]
            if new_node is not None:
                search(new_node, modified_nodes)
        else:
            not_found = True
            current_node = new_node[-2]
            next_node = new_node[-1]
            visited_nodes = set(new_node)
            current_path = list(new_node)
            for node2 in modified_nodes:
                if (
                    current_node is node2[0]
                    and node2[1] is next_node
                    and node2[2] is None
                ):
                    not_found = False
                    path_list.append(current_path.copy())
                elif (
                    node2[0] is current_node
                    and node2[1] is next_node
                    and node2[2] is not None
                    and node2[2] not in visited_nodes
                ):
                    current_path.append(node2[2])
                    visited_nodes.add(node2[2])
                    current_node = node2[1]
                    next_node = node2[2]
            new_node = None

            if not_found:
                record = tuple(current_path.copy())
                flag = record[:-3]
                new_node = modified_nodes[modified_nodes.index(record[-3:]) + 1]
                new_node = flag + new_node

            while not_found:
                for node3 in modified_nodes:
                    if (
                        current_node is node3[0]
                        and node3[1] is next_node
                        and node3[2] is None
                    ):
                        not_found = False
                        if current_path.copy() not in path_list:
                            path_list.append(current_path.copy())
                    elif (
                        node3[0] is current_node
                        and node3[1] is next_node
                        and node3[2] is not None
                        and node3[2] not in visited_nodes
                    ):
                        current_path.append(node3[2])
                        visited_nodes.add(node3[2])
                        current_node = node3[1]
                        next_node = node3[2]

            if new_node is not None:
                search(new_node, modified_nodes)

    else:
        return


def construct_tree(paths):
    tree = {}
    for path in paths:
        current = tree
        for node in path:
            current = current.setdefault(node, {})
    return tree


# Output all path structures of a multiway tree
def print_paths(tree, path=[]):
    if not tree:
        print(" -> ".join(map(str, path)))
    for node in tree:
        print_paths(tree[node], path + [node])


path_list = []
for node in modified_nodes:
    if node[0] is None:
        search(node, modified_nodes)


print(path_list)
print("--------------------")

# Print result paths
tree = construct_tree(path_list)
print_paths(tree)

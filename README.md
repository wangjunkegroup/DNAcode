
1. **System requirements**: This code can be run on windows operating system which install the environment variable for Python 3.8 or above. You can check the Python version on your local machine by using the command `python --version`.It has been tested on windows 10 and 11.

2. **Installation guide**: Download and unzip the file `Program for windows.rar`.
   
3. **Instructions for use**: Double-click the file `bulidTreeFinally.exe`.

4. **Demo**: Expected output is shown below:
 ![image](https://github.com/wangjunkegroup/DNAcode/assets/161291555/b957940e-b241-45fd-bad6-9e1ebab0a431)

The first row is the result of node partitioni for seven-node Hamiltonian gragh. The second row is the initial result of the path traversal. The third row shows the path traversal results obtained after integration.

5. **pseudocode**:
 Class Graph:
    Method add_edge(u, v):
        # Add an edge to the graph

    Method find_paths(length):
        # Find all possible paths in the graph

    Method remove_last_if_equal(paths):
        # Remove nodes if the last node is equal to the first

Function read_adjacency_matrix_from_file(file_path):
    # Read adjacency matrix data from a file

Function search(new_node, modified_nodes):
    # Perform depth-first search to find all possible paths

Function construct_tree(paths):
    # Construct a multiway tree based on the paths

Function print_paths(tree, path=[]):
    # Print the paths in the tree structure

# Read adjacency matrix data from a file
adj_matrix = read_adjacency_matrix_from_file("./adjacency_matrix.txt")

# Create an empty directed graph object
g = Graph()

# Add edges to the directed graph based on the adjacency matrix
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            g.add_edge(i, j)

# Find all possible paths in the graph
nodes = g.find_nodes(len(adj_matrix))
modified_nodes = g.remove_last_if_equal(nodes)

# Initialize an empty list to store the paths
path_list = []

# Perform a search for each node to find all paths
for node in modified_nodes:
    if node[0] is None:
        search(node, modified_nodes)

# Construct a tree based on the paths
tree = construct_tree(path_list)

# Print the paths in the tree structure
print_paths(tree)

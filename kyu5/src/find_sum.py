"""Module to solve the code-kata https://www.codewars.com/kata/biggest-sum/

We define a helper functions:

    bellman_ford():
    uses to helper functions, initialize and relax to find the shortest path

    make_node_matrix():
    to make a matrix holding tuples of node names and values to be inputted
    into a graph

    make_graph_from_matrix():
    convert a matrix into a graph to be inputted into a shortest path algorith
"""


def initialize(graph, source):
    """Set up each node within the graph where we assume that rest of the nodes
    are very far away."""
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    """Check if the distance between node and neighbour is lower than the one
    we know of and record if it is."""
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    """Returns two dictionaries, d and p where d holds all nodes and the cost
    to reach each one and p holds the predecessors which show which path
    to take each node with the lost cost."""
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until it converges
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    #check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def make_node_matrix(matrix):
    """Convert input matrix to matrix of tuples with node name and value to be
    input into function to convert to graph. Values are inverted for input
    into shortest path algorithm."""
    node_names = ['n{0}'.format(p) for p in range(1, len(matrix)**2 + 1)]
    nodes = zip(node_names, [ -n for row in matrix for n in row])
    node_matrix = []
    for i in range(len(matrix)):
        sub_list = []
        for idx, t in enumerate(nodes):
            sub_list.append(t)
            if idx == len(matrix) - 1:
                break
        node_matrix.append(sub_list)
    return node_matrix


def make_graph_from_matrix(grid):
    """Convert an input matrix of tuples into a graph where we assume the
    direction of traversal in the matrix only allowed to be one to the right
    or down."""
    graph= {}
    for row_count, row in enumerate(grid):
        for col, node in enumerate(row):
            vertex = {}
            ref, value = node
            if col == len(row) - 1:
                if row_count == len(grid) - 1:
                    key, value = grid[len(grid) - 1][len(grid) -1]
                    graph[key] = vertex
                    break
                key, value = grid[row_count + 1][col]
                vertex[key] = value
            elif row_count == len(grid) - 1:
                key, value = grid[row_count][col + 1]
                vertex[key] = value
            else:
                vertex.update([grid[row_count][col + 1], grid[row_count + 1][col]])
            graph[ref] = vertex
    return graph

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_sum(m):
    """Find the highest sum in a matrix from top left to bottom right."""
    node_matrix = make_node_matrix(m)
    graph = make_graph_from_matrix(node_matrix)
    last_node = 'n' + str(len(m) ** 2)
    paths = find_all_paths(graph, 'n1', last_node)
    costs = []
    for path in paths:
        sum = m[0][0]
        for n1, n2 in pairwise(path):
            sum += graph[n1][n2]
        costs.append(sum)
    return max(costs)

    # d, p = bellman_ford(graph, 'n1')
    # last_node = 'n' + str(len(m) ** 2)
    # return abs(d[last_node]) + m[0][0]

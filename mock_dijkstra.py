from queue import PriorityQueue
import math

nodeNum = 10

updated = PriorityQueue()

nodes = {}

graph = {}

paths = {}

# Initialize the distance of each node to infinity
def set_nodes(nodes):
    for ch in range(ord('A'), ord('H')+1):
        nodes[chr(ch)] = math.inf



def create_graph(graph):
    # graph['A'] = [['B', 5], ['D', 6], ['H', 20]]
    # graph['B'] = [['C', 4]]
    # graph['C'] = [['H', 4], ['D', 2]]
    # graph['D'] = [['E', 1], ]
    # graph['E'] = [['C', 1], ['F', 4]]
    # graph['F'] = [['G', 1]]
    # graph['G'] = [['H', 1]]

    # Question 7.1.A
    # graph['A'] = [['B',2], ['D', 5]]
    # graph['B'] = [['C', 7], ['D', 8]]
    # graph['C'] = [['F', 1]]
    # graph['D'] = [['C', 2], ['E',4]]
    # graph['E'] = [['D', 6], ['F', 3]]

    # Question 7.1.B
    # graph['A'] = [['B',10]]
    # graph['B'] = [['D', 20]]
    # graph['C'] = [['B', 1]]
    # graph['D'] = [['C', 1], ['E',30]]

    # Question 7.1.C
    graph['A'] = [['B',2], ['C', 2]]
    graph['B'] = [['C', 2]]
    graph['C'] = [['D', 2], ['E', 2]]
    graph['D'] = [['B', -1], ['E',2]]

def initialize_paths(paths):
    for ch in range(ord('A'), ord('H')+1):
        paths[chr(ch)] = []

def update_neighbors(src, dist):
    # Iterate over the neighbor nodes
    if src in graph:
        for [node, wei] in graph[src]:
            # If arrival to this node is faster than via the src node
            # Update the distance of the node and push to the stack
            if dist + wei < nodes[node]:
                # Update the distance
                nodes[node] = dist + wei
                # Put the distance-node into queue
                updated.put((nodes[node], node))
                paths[node] = paths[src] + [src]

# This algo is not a true dijkstra. Because in this algo nodes can be 
# processed multiple times. This helps the algo to work with loops and
# negative weighted edges. But the complexity is greater than O(V + E)
# for sure.
def mock_dijkstra(src, dest):
    nodes[src] = 0
    updated.put((nodes[src], src))

    # Pop nodes one by one and work on them
    while not updated.empty():
        (far, cur) = updated.get()

        # If this tuple includes a distance no longer valid, do not even
        # continue the calculation
        if far != nodes[cur]:
            continue

        update_neighbors(cur, nodes[cur])

    print("Distance of node {} is {}".format(dest, nodes[dest]))
    print("Path from node {} to node {} is {}".format(src,dest, paths[dest]+ [dest]))


if __name__ == "__main__":
    set_nodes(nodes)
    create_graph(graph)
    initialize_paths(paths)

    print(graph)
    print(nodes)

    mock_dijkstra('A', 'H')

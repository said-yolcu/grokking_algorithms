# Dijkstra's algo
# 1. Find the node with the shortest_path
# 2. Update the paths of neighbors
# 3. Repeat this for every node
# 4. Calculate the final path

import mock_dijkstra as modi
from queue import PriorityQueue

parent = {}

graph = {}

nodes = {}

processed = []

q = PriorityQueue()

def dijkstra(src, dest):
    q.put((nodes[src], src))

    while not q.empty():
        (orig, cur) = q.get()

        # print(orig, cur)

        # We may have reached to dest
        if cur == dest:
            return True
        # Check whether the cur node is in graph and not yet processed
        if cur in graph and cur not in processed:
            # It is now about to be processed
            processed.append(cur)
            # Get the neighbors of current node
            for [node, wei] in graph[cur]:
                # If it is not processed yet and the distance via cur is less
                if node not in processed and \
                    orig +wei < nodes[node]:

                    # Update the distance and parent
                    nodes[node] = orig+ wei
                    parent[node] = cur
                    q.put((nodes[node], node))

    # We cannot reach to the destination
    return False

def print_parents(dest):
    if dest is None:
        return
    
    print_parents(parent[dest])
    print(" -> {} ".format(dest), end="")

if __name__ == "__main__":
    modi.create_graph(graph)
    modi.set_nodes(nodes)

    print(graph)

    src = 'A'
    dest = 'E'
    nodes[src] = 0
    parent[src] = None

    if not dijkstra(src, dest):
        print("Cannot reach from {} to {}".format(src, dest))
    else:
        print_parents(dest)
        print()
        print(nodes[dest])

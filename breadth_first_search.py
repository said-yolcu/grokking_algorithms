import math
from queue import Queue


# Node for a graph with weightless edges
class Node:
    def __init__(self, id):
        self.id = id
        self.dist = math.inf
        self.path = []
        self.neigh = []

    def connect(self, nodes):
        for node in nodes:
            self.neigh.append(node)

    def biconnect(self, nodes):
        for node in nodes:
            self.neigh.append(node)
            node.neigh.append(self)


# Weightless graph shortest path finder
def shortest_path(src, dest):
    q = Queue()
    src.dist = 0

    # Put the src node to the queue
    q.put(src)

    # While q is not empty
    while not q.empty():
        cur = q.get()

        # Check the current node
        if cur.id == dest.id:
            return cur.path + [cur.id]

        # Iterate over the neighbors
        for neigh in cur.neigh:
            # If distance via current node is less than neighbor distance
            # Update the neighbor distance and add it to the queue.
            if cur.dist + 1 < neigh.dist:
                neigh.dist = cur.dist + 1
                neigh.path = cur.path + [cur.id]
                q.put(neigh)

    print("Dest is not in graph")
    return None

# Create a directed graph
def create_graph():
    nodeArr = [Node(i) for i in range(10)]

    nodeArr[0].connect(nodeArr[0:5])
    nodeArr[1].connect([nodeArr[5]])
    nodeArr[2].connect([nodeArr[5]])
    # nodeArr[3].connect(nodeArr[6:8])
    # nodeArr[4].connect([nodeArr[8]])
    nodeArr[5].connect([nodeArr[6], nodeArr[9]])
    # nodeArr[6].connect([nodeArr[7], nodeArr[9]])
    nodeArr[7].connect([nodeArr[6], nodeArr[8]])
    nodeArr[8].connect([nodeArr[7], nodeArr[9]])
    nodeArr[9].connect([nodeArr[8]])

    return nodeArr


if __name__ == "__main__":
    nodeArr = create_graph()

    path = shortest_path(nodeArr[0], nodeArr[7])

    print("path from {} to {} is {}".format(0, 9, path))

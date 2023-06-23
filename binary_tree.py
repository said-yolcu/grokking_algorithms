class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self) -> str:
        return str(self.val)

    def add_left(self, left):
        # Add left child to the node
        self.left = left

    def add_right(self, right):
        # Add right child to the node
        self.right = right


def insert_node(root, new_val):
    # Insert value "new_val" to the tree with root

    # Given the "root" of the tree, insert the "node"
    if root == None:
        print("None node error")
        return
    elif new_val < root.val:
        # If left child is none, fill it with value
        if root.left == None:
            root.left = Node(new_val)
            return

        insert_node(root.left, new_val)
    elif new_val > root.val:
        # If right child is none, fill it with value
        if root.right == None:
            root.right = Node(new_val)
            return

        insert_node(root.right, new_val)


def search_node(root, val, path=""):

    if root == None:
        return (False, "{} is not in the tree".format(val))
    # If the val is equal to root.val
    elif root.val == val:
        return (True, path)

    # If the val is less than root.val
    elif val < root.val:
        path += "l"
        return search_node(root.left, val, path)

    # If the val is greater than root.val
    else:  # val > root.val
        path += "r"
        return search_node(root.right, val, path)


# def delete_node(root, val):

#     (b, path) = search_node(root, val)

#     # If the searched val is not in tree, return with a notice
#     if not b:
#         return (False, root)

#     # Else, the val is in tree
#     subtree = find_node(root, path)

#     print("the subtree starts")
#     print_tree(subtree)
#     print("the subtree ends")

#     # Delete the node from the subtree that the node is the root of
#     subtree = change_tree(subtree)

#     print("modified subtree starts")
#     print_tree(subtree)
#     print("modified subtree ends")

#     # Put the new subtree in the according place
#     root = replace_node(root, subtree, path)

#     return (True, root)


def find_node(root, path):
    # Find and return the node in the specified path

    for ch in path:
        if ch == 'l':
            root = root.left
        elif ch == 'r':
            root = root.right

    return root


def change_tree(subtree):
    # Delete the root of the subtree and replace it with the leftmost
    # descendant of right child

    # print("the subtree starts")
    # print_tree(subtree)
    # print("the subtree ends")

    print("subtree is ", subtree)

    pre_node = Node(None, subtree)

    neo = subtree
    pre_neo = pre_node
    dir = "l"

    # If it has no child
    if neo.left == None and neo.right == None:
        neo = None

        # print("modified subtree starts")
        # print_tree(subtree)
        # print("modified subtree ends")

        return neo

    # If it has no right child
    elif neo.right == None:
        pre_neo = neo
        neo = neo.left
        dir = "l"

    # If it has no left child
    elif neo.left == None:
        pre_neo = neo
        neo = neo.right
        dir = "r"

    # Else, find the leftmost descendant of the right child
    else:
        pre_neo = neo
        neo = neo.right
        dir = "r"

        while neo.left is not None:
            pre_neo = neo
            neo = neo.left
            dir = "l"

    # Now replace neo and subtree
    if dir == "l":
        print("leftside")
        pre_neo.left = change_tree(neo)
    elif dir == "r":
        print("rightside")
        pre_neo.right = change_tree(neo)

    neo.left = subtree.left
    neo.right = subtree.right
    pre_node.left = neo

    print("neo is", neo)

    # print("modified subtree starts")
    # print_tree(subtree)
    # print("modified subtree ends")

    return neo


def replace_node(root, neo, path):
    # Replace the node at the "path" of tree "root" with node "neo"

    if path == "":
        return neo

    else:
        cur = root

        for ch in path[:-1]:
            if ch == "l":
                cur = cur.left
            elif ch == "r":
                cur = cur.right

        if path[-1] == "l":
            cur.left = neo
        elif path[-1] == "r":
            cur.right = neo

    return root


def print_tree(root, depth=0):
    if root == None:
        return

    # Print right side
    print_tree(root.right, depth + 1)

    # Print blank space and root value
    print(depth*3*" ", end="")
    print(root.val)

    # Print left side
    print_tree(root.left, depth+1)


def fill_tree(root):
    insert_node(root, 5)
    insert_node(root, 6)
    insert_node(root, 8)
    insert_node(root, 2)
    insert_node(root, 23)
    insert_node(root, 12)
    insert_node(root, 2)
    insert_node(root, 3)
    insert_node(root, 7)
    insert_node(root, 11)
    insert_node(root, 14)
    insert_node(root, 24)
    insert_node(root, 9)
    insert_node(root, 10)


if __name__ == "__main__":
    root = Node(12)

    fill_tree(root)

    print_tree(root, 0)

    val = 6

    print(search_node(root, val)[1])

    print_tree(root)

    # (b, new_tree) = delete_node(root, val)

    # print("Delete node {}".format(val))

    # print_tree(new_tree)

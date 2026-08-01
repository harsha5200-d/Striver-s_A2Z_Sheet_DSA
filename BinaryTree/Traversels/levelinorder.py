from collections import deque

class Tree:
    def __init__(self,data):

        self.left = None
        self.data = data
        self.right = None

def buildTree(arr, i):

    if i >= len(arr) or arr[i] == -1:
        return None

    root = Tree(arr[i])

    root.left = buildTree(arr, i * 2 + 1)
    root.right = buildTree(arr, i * 2 + 2)

    return root

def LevelInorder(root):
    # Base case: if node is null, return empty list
    if not root:
        return []

    # Initialize a double-ended queue with the root node
    dq = deque([root])
    res = []
    
    # Process nodes level by level
    while dq:
        # Get the node from the right end of the deque
        node  =  dq.pop()

        # Add right child to deque (since we are popping from right, right child should be added first to be processed later?)
        # Wait, this logic seems strange, but commenting what it does
        while node.right:
            dq.append(node.right)

        # Add left child to deque
        while node.left:
            dq.append(node.left)

        # Append current node data to result
        res.append(node.data)


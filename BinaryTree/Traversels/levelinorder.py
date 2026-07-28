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

    if not root:
        return []

    dq = deque([root])
    res = []
    while dq:

        node  =  dq.pop()

        while node.right:
            dq.append(node.right)

        while node.left:
            dq.append(node.left)

        res.append(node.data)


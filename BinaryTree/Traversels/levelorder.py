from collections import deque

class Tree:

    def __init__(self, data):
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


def levelorder(root):

    if root is None:
        return []

    result = []
    dq = deque([root])

    while dq:
        node = dq.popleft()      # Remove from front
        result.append(node.data)

        if node.left:
            dq.append(node.left)

        if node.right:
            dq.append(node.right)

    return result


arr = [1, 34, 21, 43, 11, 32]
root = buildTree(arr, 0)

res = levelorder(root)
print(res)
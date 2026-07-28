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

def maxdepth(root):

    if not root:
        return 0

    else:
        return 1 + max(maxdepth(root.left),maxdepth(root.right))


arr = [3, 9, 20, -1, -1, 15, 7]
root = buildTree(arr,0)

res = maxdepth(root)
print(res)
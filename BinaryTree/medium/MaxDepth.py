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

def maxdepth(root):

    if not root:
        return 0

    else:
        return 1 + max(maxdepth(root.left),maxdepth(root.right))

def bydequemethod(root):

    dq = deque([root])
    res = []
    
    while dq:
        subpart = []
        for i in range(len(dq)):

            node = dq.popleft()
            subpart.append(node.data)

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        res.append(subpart)

    return len(res)

arr = [3, 9, 20, -1, -1, 15, 7]
root = buildTree(arr,0)
res1 = bydequemethod(root)
res = maxdepth(root)
print(res)
print(res1)
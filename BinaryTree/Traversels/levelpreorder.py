from collections import deque

class Tree:

    def __init__(self,data):

        self.left = None
        self.data = data
        self.right = None

def BuildTree(arr,i):

    if(i>=len(arr) or arr[i]==-1):
        return None

    root = Tree(arr[i])

    root.left = BuildTree(arr,i*2+1)
    root.right = BuildTree(arr,i*2+2)

    return root

def LevelPreOrder(root):


    dq = deque([root])
    res = []
    while dq:

        node = dq.pop()
        res.append(node.data)

        if node.right:
            dq.append(node.right)

        if node.left:
            dq.append(node.left)

    return res

arr = [1, 34, 21, 43, 11, 32]
root = BuildTree(arr, 0)

res = LevelPreOrder(root)
print(res)

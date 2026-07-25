from collections import deque

class Tree:

    def __init__(self,data):

        self.left = None
        self.data = data
        self.right = None

def buildTree(arr,i):

    if(i>=len(arr) or arr[i]==-1):
        return None


    root = Tree(arr[i])

    root.left = buildTree(arr,i*2+1)
    root.right = buildTree(arr,i*2+2)

    return root


def levelorder(root):

    levelorder = []
    de = deque([root])
    while de:
        for i in range(len(de)):
            node = de.popleft()
            levelorder.append(node.data)
            if node.left:
                de.append(node.left)
            if node.right:
                de.append(node.right)

    return levelorder

arr = [1,34,21,43,11,32]
root = buildTree(arr,0)
res = levelorder(root)
print(res)






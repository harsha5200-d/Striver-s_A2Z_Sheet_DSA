class Tree:

    def __init__(self,data):

        self.left = None
        self.data = data
        self.right = None


def buildTree(arr,i):

    if(len(arr)<=i or arr[i]==-1):
        return None
    

    root = Tree(arr[i])
    root.left = buildTree(arr,i*2+1)
    root.right = buildTree(arr,i*2+2)


    return root

def postorder(root):

    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
root = buildTree(arr,0)
postorder(root)





    
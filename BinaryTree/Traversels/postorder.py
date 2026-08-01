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
    # Base case: if node is null, stop recursion
    if not root:
        return None

    # Postorder traversal logic: Left -> Right -> Root
    postorder(root.left)   # Recursively visit left subtree
    postorder(root.right)  # Recursively visit right subtree
    print(root.data,end=" ") # Visit the root node


arr = [1, 2, 3, 4, 5, 6, 7]
root = buildTree(arr,0)
postorder(root)





    
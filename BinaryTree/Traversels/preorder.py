class Tree:
    def __init__(self,data):
        self.left = None
        self.data= data
        self.right = None

def BuildTree(arr,i):
    if (i>=len(arr) or arr[i]==-1):
        return None

    root = Tree(arr[i])

    root.left = BuildTree(arr,i*2+1)
    root.right = BuildTree(arr,i*2+2)
    return root

def preorder(root):

    if not root:
        return []
    
    return [root.data] + preorder(root.left)  + preorder(root.right)

arr = [1 ,2, 4, 5, 3, 6, 7]
root = BuildTree(arr,0)
res = preorder(root)
print(res)


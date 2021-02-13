# Class representation of binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def printtree(self):
        print(self.value)

# tree traversals - recursive
def inorderTraversal(root):
    return inorderTraversal(root.left) + [root.value] + inorderTraversal(root.right) if root else []

def preorderTraversal(root):
    return [root.value] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []

def postorderTraversal(root):
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.value] if root else []


a = TreeNode(27)
b = TreeNode()
c = TreeNode(34)
d = TreeNode(3)
e = TreeNode(8)
f = TreeNode(3334)

a.left = b
a.right = c
b.right = d
d.left = e
c.right = f

print(postorderTraversal(a))

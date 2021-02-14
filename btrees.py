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


# tree traversals - iterative
def inorderIterative(root):
    stack = []
    res = []
    if not root:
        return []
    stack.append(root)
    root = root.left
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        res.append(node.value)
        root = node.right
    return res

def preorderIterative(root):
    #method 1
    stack = []
    res = []
    if not root:
        return []
    stack.append(root)
    res.append(root.value)
    root = root.left
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.value)
            root = root.left
        node = stack.pop()
        root = node.right
    return res

    # method 2
    ### storing only right side in stack
    # stack = []
    # res = []
    # curr = root
    # if not root:
    #     return None
    # while stack or curr:
    #     if not curr:
    #         curr = stack.pop()
    #     while curr:
    #         res.append(curr.value)
    #         if curr.right:
    #             stack.append(curr.right)
    #         curr = curr.left
    # return res
        
    # method 3
    # if not root:
    #     return []
    # stack.append(root)
    # while stack:
    #     root = stack.pop()
    #     res.append(root.value)
    #     if root.right:
    #         stack.append(root.right)
    #     if root.left:
    #         stack.append(root.left)
    # return res

def postorderIterative(root):
    res = []
    st = []
    st.append(root)
    while st:
        root = st.pop()
        res.append(root.value)
        if root.left:
            st.append(root.left)
        if root.right:
            st.append(root.right)

    res.reverse()
    return res


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

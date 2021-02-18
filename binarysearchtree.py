from treesDs import TreeNode, inorderIterative
# insert, search, delete, print path

# Insert Node in BST - iterative and recursive


def insertNodeIterative(root, key):
    if root is None:
        return TreeNode(key)
    # assign root to temporary variable 'node' that traverses the tree
    node = root

    while node:
        temp = node  # used to store the parent node of node_to_be_inserted
        if key <= node.value:
            node = node.left
        elif key > node.value:
            node = node.right

    if temp.value >= key:
        temp.left = TreeNode(key)
    else:
        temp.right = TreeNode(key)
    # node = TreeNode(key)
    return root


def insertRecursive(root, key):
    if not root:
        return TreeNode(key)
    elif root.value >= key:
        root.left = insertRecursive(root.left, key)
    elif root.value < key:
        root.right = insertRecursive(root.right, key)
    return root
#################################################################################################################################
# Search node in the BST return the subtree rooted with that node as inorder traversal.
# If not found, return -1


def searchNode(root, key):
    def findNodeIterative(root, key):
        if root is None:
            return -1
        while root:
            if root.value == key:
                return root
            elif root.value > key:
                root = root.left
            else:
                root = root.right
        return -1

    def findNodeRecursive(root, key):
        if not root:
            return -1
        elif root.value == key:
            return root
        elif root.value > key:
            return findNodeRecursive(root.left, key)
        else:
            return findNodeRecursive(root.right, key)

    # node = findNodeIterative(root, key)
    node = findNodeRecursive(root, key)
    return inorderIterative(node) if node != -1 else -1


#################################################################################################################################
# delete node in BST - iterative


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        parent, node = self.findNode(root, key)
        
        #node does not exist
        if node == -1:
            return root
        #no children
        elif node.left == None and node.right == None:
            if parent == None:
                return None
            else:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
        #1 child
        elif node.left == None and node.right != None:
            if parent == None:
                return node.right
            else:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return root
        #1 child       
        elif node.left != None and node.right == None:
            if parent == None:
                return node.left
            else:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return root
        #2 child
        elif node.left != None and node.right != None:
            temp = self.smallestrightnode(node.right)
            if parent == None: #root node to be deleted
                node.val = temp.val
                p, n = self.findNode(node.right, temp.val)
                if p == None:
                    node.right = n.right
                else:
                    p.left = n.right
            else:
                node.val = temp.val
                p, n = self.findNode(node.right, temp.val)
                if p == None:
                    node.right = n.right
                else:
                    p.left = n.right
            return root
                
                
    def findNode(self, root, key):
        parent = None
        while root:
            if root.val == key:
                return (parent, root)
            parent = root
            if root.val > key:
                root = root.left
            else:
                root = root.right
        return (-1, -1)
    
    def smallestrightnode(self, root):
        res = root
        while root:
            res = root
            root = root.left
        return res
#################################################################################################################################

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

b.left = a
b.right = c

print("before inserting", inorderIterative(b))
ans = insertNodeIterative(b, 100)
print("after inserting ", inorderIterative(ans))
print(searchNode(b, 30))

from treesDs import TreeNode, inorderIterative

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
# delete node in BST
# Step1 : find if node exists or not
# Step 2 - delete the node based on 3 categories a) leaf node b) has only one child c) has both child

def deleteNodeIterative(root,key):
    if not root:
        return root

    parent, node = findNode(root, key)
    
    #node does not exist
    if node == -1:
        return root

    #no children
    elif node.left == None and node.right == None:
        if parent == None: #node to be deleted is root and has no children, return empty tree
            return None
        else: #parent exists
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return root

    #1 child - right
    elif node.left == None and node.right != None:
        if parent == None: #node to be deleted is root and node has only right child
            return node.right
        else:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            return root
    #1 child - left 
    elif node.left != None and node.right == None:
        if parent == None: #node to be deleted is root and node has only left child
            return node.left
        else:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return root

    #2 child - replace the node value with smallest node in the right subtree, traverse the right subtree
    # and delete that smallest node(or the leftmost node)
    elif node.left != None and node.right != None:
        temp = smallestrightnode(node.right)
        node.value = temp.value
        p, n = findNode(node.right, temp.value)
        if p == None:
            node.right = n.right
        else:
            p.left = n.right
        return root

# ---------helper functions--------------------
#finds if node is in subtree- returns (parent, node) if key exists in the tree
# if not found returns (-1,-1)
def findNode(root, key):
    parent = None
    while root:
        if root.value == key:
            return (parent, root)
        parent = root
        if root.value > key:
            root = root.left
        else:
            root = root.right
    return (-1, -1)

#returns the smallest node in the right subtree of node - called only when node to be deleted has both left and right children
def smallestrightnode(node):
    res = node
    while node:
        res = node
        node = node.left
    return res


def deleteNodeRecursive(root, key):
    if root is None:
        return None
    if root.value == key:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            node = root.right
            while node.left:
                node = node.left
            root.value = node.value
            root.right = deleteNodeRecursive(root.right, node.value)
    elif root.value > key:
        root.left = deleteNodeRecursive(root.left, key)
    else:
        root.right = deleteNodeRecursive(root.right, key)
    return root
#################################################################################################################################

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(10)
d = TreeNode(8)
b.left = a
b.right = c
c.left = d

print("before inserting", inorderIterative(b))
ans = insertNodeIterative(b, 100)
print("after inserting ", inorderIterative(ans))
print(inorderIterative(b))
node = (deleteNodeIterative(b, 878))
print(inorderIterative(node))

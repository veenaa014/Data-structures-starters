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
# delete node in BST
# def deleteNodeBST(root, key):


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

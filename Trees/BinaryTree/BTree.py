class TreeNode:
    # Initialize  left, right, and value
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


BinaryTree = TreeNode('Drinks')
LeftChild = TreeNode("Cold")
RightChild = TreeNode("Hot")
BinaryTree.left = LeftChild                                             # Drinks
BinaryTree.right = RightChild                                   # Cold               Hot
LeftChild = TreeNode("coke")                              # coke    # pepsi  #espresso  # latte
RightChild = TreeNode("pepsi")
BinaryTree.left.left = LeftChild
BinaryTree.left.right = RightChild
LeftChild = TreeNode("espresso")
RightChild = TreeNode("latte")
BinaryTree.right.left = LeftChild
BinaryTree.right.right = RightChild


def preOrderTraversal(root):
    #Check that the root exists
    if not root:
        return
    print(root.data) 
    # Recursively call preOrderTraversal for the left 
    preOrderTraversal(root.left)
    # Revursively call preOrder Traversal for the right
    preOrderTraversal(root.right)

def inOrderTraversal(root):
    #Check that the root exists:
    if not root:
        return
    # Recursively call inOrderTraversal for the left
    inOrderTraversal(root.left)
    print(root.data)
    # Recursively call inOrderTraversal for the left
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    # Check that root exists
    if not root:
        return 
    # Recursively call postOrdrTraversal for the left
    postOrderTraversal(root.left)
        # Recursively call postOrdrTraversal for the right
    postOrderTraversal(root.right)
    print(root.data)
postOrderTraversal(BinaryTree)
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None



class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if(self.LinkedList.head == None):
            return True
        else:
            return False
        
    def enqueue(self, value):
        newNode = Node(value)
        if (self.isEmpty()):
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def dequeue(self):
        if(self.isEmpty()):
            return 'Queue is empty'
        else:
            currentNode = self.LinkedList.head
            if(self.LinkedList.head == self.LinkedList.tail):
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = currentNode.next
            return currentNode

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

def levelOrderTraversal(root):
    if not root:
        return 
    else:
        queue = Queue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            print(root.value.data)
            if(root.value.left is not None):
                queue.enqueue(root.value.left)
            if(root.value.right is not None):
                queue.enqueue(root.value.right)

levelOrderTraversal(BinaryTree)

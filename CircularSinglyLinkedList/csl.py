class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        # Start at head Node
        currentNode = self.head
        linkedList = ''
        headCount = 1
        # Iterate though the list 
        while currentNode:
            # if the current node is the head add a different string
            if(currentNode == self.head):
                # First iteration
                if(headCount == 1):
                    linkedList += f'[head| {currentNode.value}]'
                    headCount += 1
                # Second Iteration
                else:
                    linkedList += f' --> [head| {currentNode.value}]'
                    break
            else:
                # Print out nodes
                linkedList += f'--> {currentNode.value}'
            currentNode = currentNode.next
        return linkedList
    
    def append(self,value):
        #Create a new node
        newNode = Node(value)
        # Check if the head is None:
        if(self.head is None):
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode 
        # To make the linked list circular the tail points to the head
        self.tail.next = self.head
        self.length += 1

myLinkedList = CircularLinkedList()
myLinkedList.append(5)
print(myLinkedList.tail.next.value)
myLinkedList.append(7)
print(myLinkedList)
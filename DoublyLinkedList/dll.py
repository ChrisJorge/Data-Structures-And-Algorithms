class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def __str__(self):
        # Initialize A pointer
        currentNode = self.head
        # Initialize An output String
        DLL = ''
        # Iterate through the linked list
        while currentNode:
            if (currentNode == self.head):
                DLL += f' None <-- {currentNode.value} --> '
            else:
                # Add the current Nodes value to the output string
                DLL += f'<-- {currentNode.value} --> '
                # Iterate the node to the next one in the linked list
            currentNode = currentNode.next
        DLL += 'None'
        return DLL

    def append(self, value):
        # Create a new node
        newNode = Node(value)
        # Check if the linked list is empty
        if(self.length == 0):
            # Assign the new Node to the head and tail
            self.head = newNode
            self.tail = newNode
        else:
            # Assign the new node to the next pointer of the current tail
            self.tail.next = newNode
            # Assign the new nodes prev to the current tail
            newNode.prev = self.tail 
            # Reassign the tail so it points to the new node
            self.tail = newNode
            # Make the new tails next point to None
            self.tail.next = None
        # Increase Length by 1
        self.length += 1
    
    def prepend(self, value):
        # Create a new node
        newNode = Node(value)
        # Check if the linked list is empty
        if(self.length == 0):
            # assign the new node to the head and tail
            self.head = newNode
            self.tail = newNode
        else:
            # Assign the new nodes next pointer to the current head
            newNode.next = self.head
            # assign the current heads previous pointer to the new node
            self.head.prev = newNode
            # assign the head to the new Node
            self.head = newNode
            # assign the newNodes prev pointer to None
            newNode.prev = None
        # Increase Length by 1
        self.length += 1

    def search(self,target):
        # Check if the linked list has values
        if(self.length == 0):
            return False
        else:
            index = 0
            currentNode = self.head
            # Iterate through the linked list
            for _ in range(self.length):
                # Check if the current nodes value is the target
                if(currentNode.value == target):
                    return True, index
                else:
                    # Iterate the current node and increment index
                    currentNode = currentNode.next
                    index += 1
            # If the value is not inside of the linked list return false
            return False

myLinkedList = DoublyLinkedList()
myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.append(105)
myLinkedList.prepend(33)
myLinkedList.prepend(3)
print(myLinkedList)
print(myLinkedList.search(3))
print(myLinkedList.search(105))
print(myLinkedList.search(5))
print(myLinkedList.search(51))
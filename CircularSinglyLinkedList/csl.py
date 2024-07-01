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
        if(self.length == 0):
            return 'Linked List Is Empty'
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
        # Create a new node
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

    def prepend(self,value):
        # Create a new node
        newNode = Node(value)

        # Check if the head is None:
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.tail.next = newNode
        self.length += 1

    def insert(self,index,value):
        # if index is invalid return invalid index
        if(index > self.length or index < 0):
            return 'Invalid Index'
        # if the index is 0 append to the front of linked list
        elif(index == 0):
            return self.prepend(value)
        # If the index is at the end append to the linked list
        elif(index == self.length):
            return self.append(value)
        else:
            currentIndex = 0
            currentNode = self.head
            # while the current node is valid and the index is less than the specified index - 1
            while currentIndex < index - 1 and currentNode:
                # increment the current node
                currentNode = currentNode.next
                # increase the currentIndex by 1
                currentIndex += 1
            newNode = Node(value)
            # create a temp node to keep connection to rest of linked list
            temp = currentNode.next
            # set the current nodes next to the new node
            currentNode.next = newNode
            # make the new nodes next the temp node
            newNode.next = temp
            # increase the length by 1
            self.length += 1

    def search(self, target):
        currentNode = self.head
        # iterate through the nodes
        while currentNode:
            # if the value is in the linked list return true
            if(currentNode.value == target):
                return True
            # if the current node isnt the value iterate to the next node
            currentNode = currentNode.next
            # if the head is reached again the whole linked list has been checked, return false
            if(currentNode == self.head):
                return False

    def get(self,index):
        # Check if index is valid
        if(index > self.length - 1 or index < 0):
            return 'Invalid Index'
        # Check if index is head
        elif(index == 0):
            return self.head.value
        elif(index == self.length - 1):
            return self.tail.value
        else:
            currentNode = self.head
            # iterate through until the index
            for _ in range(index):
                currentNode = currentNode.next
            # Return the value
            return currentNode.value

myLinkedList = CircularLinkedList()
myLinkedList.prepend(5)
myLinkedList.prepend(10)
myLinkedList.prepend(90)
myLinkedList.prepend(92)
myLinkedList.append(9)
myLinkedList.append(10)
myLinkedList.append(11)
print(myLinkedList)
print(myLinkedList.get(0))
print(myLinkedList.get(3))
print(myLinkedList.get(5))

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
    
    def set(self,index,value):
        # Check if index is valid
        if(index > self.length - 1 or index < 0):
            return 'Invalid Index'
        # If the index is the head
        elif(index == 0):
            # Change the head value
            self.head.value = value
        # If the index is the tail
        elif(index == self.length - 1):
            # Change the tail value
            self.tail.value = value
        else:
            currentNode = self.head
            # Iterate through the linked list
            for _ in range(index):
                currentNode = currentNode.next
            # Change the value
            currentNode.value = value
    
    def popFirst(self):
        poppedNode = self.head
        #Check the length of linked list
        if(self.length == 0):
            # If length is zero linked list is empty
            return 'Linked List Is Empty'
        elif(self.length == 1):
            # if length is 1 set head and tail to none
            self.head = None
            self.tail = None
        elif(self.length == 2):
            # if length is 2 set head to the next node and tail to the same node
            self.head = self.head.next
            self.tail = self.head
            self.tail.next = self.head
        else:
            self.head = self.head.next
            self.tail.next = self.head
        # decrease the length by 1
        self.length -= 1
        return poppedNode.value
    
    def pop(self):
        # Get the node to be removed
        poppedNode = self.tail
        # Check length of linked list
        if(self.length == 0):
            return 'Linked List Is Empty'
        elif(self.length == 1):
            self.head = None
            self.tail = None
        elif(self.length == 2):
            self.tail = self.head
            self.tail.next = self.head
        else:
            currentNode = self.head
            # Iterate until one before the tail
            for _ in range(self.length - 2):
                currentNode = currentNode.next
            self.tail = currentNode
            self.tail.next = self.head
        self.length -= 1
        return poppedNode.value
    
    def remove(self,index):
        # Check if length is valid
        if(index > self.length - 1 or index < 0):
            return 'Invalid Index'
        # Check if index is head
        if(index == 0):
            return self.popFirst()
        # Check if the index is the tail
        elif(index == self.length - 1):
            return self.pop()
        else:
            currentNode = self.head
            # Iterate through linked list until 1 before the index to be removed
            for _ in range(index - 1):
                currentNode = currentNode.next
            # Get the node to be removed
            poppedNode = currentNode.next
            # Skip over the popped Node
            currentNode.next = currentNode.next.next
            # make the poppedNodes next be none to severe the connection
            poppedNode.next = None
            # Decrease length by 1
            self.length -= 1
            return poppedNode.value

myLinkedList = CircularLinkedList()
myLinkedList.prepend(5)
myLinkedList.prepend(10)
myLinkedList.prepend(90)
myLinkedList.prepend(92)
myLinkedList.append(9)
myLinkedList.append(10)
myLinkedList.append(11)
print(myLinkedList)
print(myLinkedList.remove(6))
print(myLinkedList)

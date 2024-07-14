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
            while currentNode:
                # Check if the current nodes value is the target
                if(currentNode.value == target):
                    return index
                else:
                    # Iterate the current node and increment index
                    currentNode = currentNode.next
                    index += 1
            # If the value is not inside of the linked list return false
            return -1
    
    def get(self,index):
        # Check if index is valid
        if (index < 0 or index > self.length - 1):
            return 'Invalid Index'
        else:
            # Check if index is in the first or second half of linked list
            if(index < self.length // 2):
                # Iterate through the linked list until the specified index
                currentNode = self.head
                for _ in range(index):
                    # Increment to the next node
                    currentNode = currentNode.next
            else:
                currentNode = self.tail
                # Iterate through the linked list until the specified index
                for _ in range(self.length - 1, index, -1):
                    # Icrement to the previous node
                    currentNode = currentNode.prev
            return currentNode

    def set(self,index,value):
        # Check if the index is valid
        if(index < 0 or index > self.length - 1):
            return 'Invalid Index'
        elif(index == 0):
            # If index is the head change the heads value
            self.head.value = value
        elif(index == self.length - 1):
            # If index is the tail change the tails value
            self.tail.value = value
        else:
            # Use the get method to get the node at the specified index
            currentNode = self.get(index)
            # Change the nodes value
            currentNode.value = value
        return True
    
    def insert(self,index,value):
        # Check if index is valid
        if(index < 0 or index > self.length):
            return 'Invalid Index'
        # if index is zero prepend the new node
        elif(index == 0):
            return self.prepend(value)
        # if the index is the length of the linked list append
        elif(index == self.length):
            return self.append(value)
        else:
            # Create a new node
            newNode = Node(value)
            # get the node before
            currentNode = self.get(index - 1)
            # set the newNodes next to the node at that current index
            newNode.next = currentNode.next
            # set that nodes previous to the new node
            currentNode.next.prev = newNode
            # make the newnodes previous the current node
            newNode.prev = currentNode
            # set the current nodes next to the new node
            currentNode.next = newNode
        # increase the length by 1
        self.length += 1

    def popFirst(self):
        # Check to make sure the linked list has nodes
        if(self.length == 0):
            return 'LinkedList is empty'
        elif(self.length == 1):
            poppedNode = self.head
            self.head = None
            self.tail = None
        elif(self.length == 2):
            poppedNode = self.head
            self.tail.prev = None
            self.head = None
            self.head = self.tail 
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            self.head.prev = None
        self.length -= 1
        return poppedNode.value

    def pop(self):
        # Check to make sure the linked list has nodes
        if(self.length == 0):
            return 'LinkedList is empty'
        # Check if the linked list has a length of 1
        elif(self.length == 1):
            # assign the popped node to the head
            poppedNode = self.head
            # make the head and tail pointers point to none
            self.head = None
            self.tail = None
        else:
            # assign the popped node to the tail
            poppedNode = self.tail 
            # make the new tail one before the tail
            self.tail = self.tail.prev
            # remove the connection from the old tail and the rest of the linked list
            self.tail.next = None
            poppedNode.prev = None
        # decrease length by 1
        self.length -= 1
        # return the popped nodes value
        return poppedNode.value
    
    def remove(self,index):
        # Check if the index is valid
        if ( index < 0 or index > self.length - 1):
            return 'Invalid Index'
        # Check if the index is the head
        elif (index == 0):
            return self.popFirst()
        # Check if the index is the tail
        elif (index == self.length - 1):
            return self.pop()
        else:
            # get the index to be removed
            poppedNode = self.get(index)
            nodeBefore = poppedNode.prev
            nodeAfter = poppedNode.next
            # create a connection from the node before and after the popped node
            nodeBefore.next = nodeAfter
            nodeAfter.prev = nodeBefore
            # remove the connect the popped node has from the list
            poppedNode.next = None
            poppedNode.prev = None
        # Decrease the length by 1    
        self.length -= 1
        # Return the popped nodes value
        return poppedNode.value

myLinkedList = DoublyLinkedList()
myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.append(105)
myLinkedList.prepend(33)
myLinkedList.prepend(3)
myLinkedList.insert(0,0)
myLinkedList.insert(6,0)
myLinkedList.insert(4,0)
print(myLinkedList)
print(myLinkedList.remove(0))
print(myLinkedList.remove(6))
print(myLinkedList.remove(3))
print(myLinkedList.remove(30))
print(myLinkedList)
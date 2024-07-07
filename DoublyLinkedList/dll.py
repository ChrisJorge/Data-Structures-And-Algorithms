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
        elif (index == 0):
            # If index is the head return the head value
            return self.head.value
        elif (index == self.length - 1):
            # If the index is the tail return the tail value
            return self.tail.value
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
            return currentNode.value

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
            # Change the nodes value
            currentNode.value = value
            return True


myLinkedList = DoublyLinkedList()
myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.append(105)
myLinkedList.prepend(33)
myLinkedList.prepend(3)
print(myLinkedList)
myLinkedList.set(0, 0)
myLinkedList.set(2, 1)
myLinkedList.set(4, 1000)
print(myLinkedList.set(10, 30))
print(myLinkedList)

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        
        # If empty:
        if self.head == None: 
            self.head = newNode
            return 
        
        # Traversal
        current = self.head
        while current.next != None:
            current = current.next
        
        # Add new Node
        current.next = newNode
        
        return
    
    def remove(self,data):
        # Traversal
        current = self.head
        prev = None
        while current != None and current.data != data:  # Correction: Fixed logical condition
            prev = current
            current = current.next
        
        if current == None:  # Correction: Handle case when current is None
            print("Node not Found")
            return
        
        prev.next = current.next
        current.next = None

        return
            
        
    def prepend(self,data):
        # Initialize
        newNode = Node(data)
        newNode.next = self.head  # Correction: Added self
        self.head = newNode

        return
    
    def display(self):
        current = self.head
        while current != None:  # Correction: Changed condition
            print(current.data, end="-> ")
            current = current.next
            
        print("None")
        return
    
    

# Create a singly linked list instance
sll = SinglyLinkedList()

# Test append function
sll.append(1)
sll.append(2)
sll.append(3)

# Test prepend function
sll.prepend(0)

# Display the list
print("Linked list content:")
sll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Test delete function
sll.remove(2)

# Display the list after deletion
print("\nLinked list content after deleting '2':")
sll.display()  # Output: 0 -> 1 -> 3 -> None

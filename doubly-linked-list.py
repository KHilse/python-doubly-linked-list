class DllNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        '''Adds a node to the back of the LL\n
            Usage: my_DoublyLinkedList.append(data: any)'''
        new_node = DllNode(data)
        if self.head:
            # List is not empty
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            # List is empty
            self.head = self.tail = new_node
        return True

    def remove(self, data):
        ''' Removes a node from the LL\n
                Usage: my_DoublyLinkedList.remove(data: any)'''
        current = self.tail
        while current != None:
            if current.data == data:
                if self.head == self.tail: # Special case if list has only one node
                    self.head = None
                    self.tail = None
                    return current.data 
                # Get prev Node
                if current.prev == None: # Head of list
                    self.head = current.next
                    current.next.prev = None
                elif current.next == None: # tail of list
                    current.prev.next = None
                    self.tail = current.prev
                else: # middle of list
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return current.data
            # Get next Node                
            current = current.prev
        return False

    def sortedInsert(self, data):
        '''Inserts a new node to LL in the correct sorted position\n
            Usage: my_list.sortedInsert(data: any)'''
        # Search the list for either 1) equality, or 2) an insertion point
        # between two nodes
        new_node = DllNode(data)
        if self.head == None: # Special Case empty list
            self.head = self.tail = new_node
            return
        # Edge case #2: Inserting at the head
        if self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = self.head.prev = new_node
        else:
            current = self.head
            # traverse the linked list, and find the node before the spot we want to insert @
            while current.next != None and current.next.data < data:
                current = current.next
            
            new_node.next = current.next # Set new node's relationship to the forward node

            if current.next == None:
                self.tail = new_node
                
            if current.next != None: # Set backwards relationship for the forward node
                new_node.next.prev = new_node

            current.next = new_node # Set forward relationship for the previous node
            new_node.prev = current # Set backwards relationship for the newly made node
        

    def show(self):
        '''Prints out the node data in the list in order'''
        if self.head == None:
            print('Empty')
        current = self.head
        while current:
            print(current.data)
            current = current.next

my_ll = DoublyLinkedList()
my_ll.append('Charles')
my_ll.append('Amy')
my_ll.append('Xavier')
my_ll.show()
my_ll.remove('Charles')
my_ll.show()
my_ll.remove('Xavier')
my_ll.show()
my_ll.remove('Amy')
my_ll.show()
my_ll.sortedInsert('7')
my_ll.show()
my_ll.sortedInsert('1')
my_ll.show()
my_ll.sortedInsert('3')
my_ll.show()
my_ll.sortedInsert('2')
my_ll.show()

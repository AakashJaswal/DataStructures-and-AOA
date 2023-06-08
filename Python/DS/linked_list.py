class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.data


# Linked List class contains a Node object 
class LinkedList:
    # Function to initialize head 
    def __init__(self):
        self.head = None

    def add_next(self, data):
        if not self.head:
            print("first")
            self.head = Node(data)
        else:
            curr = self.head
            print("second")
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(Node(data))

    def print(self):
        if not self.head:
            print("Empty")
        else:
            curr = self.head
            i = 1
            while curr:
                print(f"Node[{i}]=", curr.data, end=" ")
                i += 1
                curr = curr.get_next()


# Node creation
if __name__ == '__main__':
    list = LinkedList()
    list.print()
    list.add_next(2)
    list.add_next(5)
    list.print()

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
        self.head: Node = None

    def add_next(self, data):
        if self.head:
            curr = self.head
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(Node(data))
        else:
            self.head = Node(data)

    def delete(self, data):
        if self.head:
            curr = self.head
            if curr.get_data() == data:
                self.head = curr.get_next()
            else:
                while curr.get_next().get_data() != data:
                    curr = curr.get_next()
                curr.set_next(curr.get_next().get_next())

    def print(self):
        if self.head:
            curr = self.head
            i = 1
            while curr:
                print(f"Node[{i}]=", curr.data, end=" ")
                i += 1
                curr = curr.get_next()
            print()
        else:
            print("Empty")


# Node creation
if __name__ == '__main__':
    list = LinkedList()
    list.print()
    list.add_next(2)
    list.add_next(5)
    list.add_next(7)
    list.print()
    list.delete(2)
    list.print()

# TODO: add deletion & insertion based on index.

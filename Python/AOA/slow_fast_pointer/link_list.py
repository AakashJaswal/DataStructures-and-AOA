class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self, val):
        self.head = Node(val)

    def add(self, val):
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val)

    def print(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        print(res)

    def slow_fast(self):
        slow: Node = self.head
        fast: Node = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.val)


head = LinkList(0)
head.add(1)
head.add(2)
head.add(3)
head.add(4)
head.add(5)
head.print()

head.slow_fast()

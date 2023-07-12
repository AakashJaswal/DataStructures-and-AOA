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
        return curr.next

    def add_node(self, nd: Node):
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = nd
        return curr.next

    def print(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res

    def slow_fast(self):
        slow: Node = self.head
        fast: Node = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.val

    def has_cycle(self):
        slow: Node = self.head
        fast: Node = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False

    def has_cycle_return_start(self):
        slow: Node = self.head
        slow2: Node = self.head
        fast: Node = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None

        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow.val



head = LinkList(0)
head.add(1)
two = head.add(2)
head.add(3)
head.add(4)
head.add(5)

# print(head.print())
# print(f"Mid : {head.slow_fast()}")

head.add_node(two)

print(head.has_cycle())

print(head.has_cycle_return_start())
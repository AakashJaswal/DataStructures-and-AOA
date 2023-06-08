class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        self.stack.pop()

    def peek(self):
        print(self.stack[-1])


st = Stack()
st.push(2)
st.push(4)
st.peek()
st.pop()
st.peek()

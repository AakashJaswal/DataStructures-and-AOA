class Heap:
    def __init__(self):
        self.he = [0]

    def insert(self, val):
        self.he.append(val)
        i = len(self.he) - 1

        while self.he[i] < self.he[(i // 2)]:
            self.he[i], self.he[(i // 2)] = self.he[(i // 2)], self.he[i]
            i = i // 2

    def pop(self):
        if len(self.he) == 0:
            return None
        if len(self.he) == 1:
            return self.he.pop()

        res = self.he[1]
        self.he[1] = self.he.pop()

        i = 1

        while (i * 2) < len(self.he):
            if (i * 2 + 1) < len(self.he) and self.he[(i * 2 + 1)] < self.he[i * 2] and self.he[i] > self.he[
                (i * 2 + 1)]:
                # right exists, it's less than left and he[1] is greater than right child
                self.he[i], self.he[(i * 2 + 1)] = self.he[(i * 2 + 1)], self.he[i]
                i = i * 2 + 1
            elif self.he[i] > self.he[i * 2]:
                # left is greater than child
                self.he[i], self.he[(i * 2)] = self.he[(i * 2)], self.he[i]
                i = i * 2
            else:
                break
        return res


a = Heap()
a.insert(30)
a.insert(65)
a.insert(68)
a.insert(19)
a.insert(26)

print(a.pop())
print(a.pop())

from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def create_BST(val: list[int]):
    def insert(root, el):
        if not root:
            return TreeNode(el)
        if el < root.val:
            root.left = insert(root.left, el)
        if el > root.val:
            root.right = insert(root.right, el)
        return root

    root = insert(None, val[0])
    for idx in range(1, len(val)):
        insert(root, val[idx])
    return root





def dfs(root: TreeNode):
    if not root:
        return None
    dfs(root.left)
    res.append(root.val)
    dfs(root.right)


def bfs(root):
    q = deque()
    if root:
        q.append(root)
    level = 0
    while len(q) > 0:
        print(f"Level : {level}")
        for i in range(len(q)):
            curr = q.popleft()
            print(curr.val, end=' ')
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        print()
        level += 1


if __name__ == '__main__':
    root = create_BST([3, 2, 1, 4, 5])
    print(root.val)

    res = []
    dfs(root)
    print(res)

    bfs(root)

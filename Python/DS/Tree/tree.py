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


def traverse_boundary(root):
    res = []

    def dfs_left(node):
        if not node.left and not node.right:
            return
        res.append(int(node.val))
        if node.left:
            dfs_left(node.left)
        else:
            dfs_left(node.right)

    def dfs_right(node):
        if not node.left and not node.right:
            return
        res.append(int(node.val))
        if node.right:
            dfs_left(node.right)
        else:
            dfs_left(node.left)

    def inorder(node):
        if not node:
            return
        if not node.left and not node.right:
            res.append(int(node.val))
            return

        inorder(node.left)
        inorder(node.right)

    dfs_left(root)
    inorder(root)
    if root.right:
        dfs_right(root.right)
    return res


if __name__ == '__main__':
    root = create_BST([3, 2, 1, 4, 5])
    print(root.val)

    res = []
    dfs(root)
    print(res)

    bfs(root)

    print()
    print(traverse_boundary(root))

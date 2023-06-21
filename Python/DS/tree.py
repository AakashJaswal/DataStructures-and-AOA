class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def create_BST(val: list[int]):
    root = TreeNode(val[0])
    curr = root
    for i in range(1, len(val)):
        if val[i] < curr.val:
            while curr.left:
                curr = curr.left
            curr.left = TreeNode(val[i])
        else:
            while curr.right:
                curr = curr.right
            curr.right = TreeNode(val[i])
        curr = root
    return root


root = create_BST([3, 2, 1, 4, 5])
print(root.val)

res = []


def dfs(root: TreeNode):
    if not root:
        return None
    dfs(root.left)
    res.append(root.val)
    dfs(root.right)


dfs(root)
print(res)

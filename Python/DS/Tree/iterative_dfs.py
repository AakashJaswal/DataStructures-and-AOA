from tree import create_BST, TreeNode

arr = [4, 2, 1, 3, 6, 5, 7]

root = create_BST(arr)


def iterative_preorder_dfs(root: TreeNode):
    q = [root]
    res = []
    while q:
        node: TreeNode = q.pop()
        res.append(node.val)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return res


def iterative_inorder_dfs(root: TreeNode):
    q = []
    res = []
    curr = root
    while q or curr:
        while curr:
            q.append(curr)
            curr = curr.left
        curr: TreeNode = q.pop()
        res.append(curr.val)
        curr = curr.right

    return res


print(iterative_preorder_dfs(root))
print(iterative_inorder_dfs(root))

package Trees.HandsOn;

public class TreeNode<T> {
    private T data;
    private TreeNode<T> left;
    private TreeNode<T> right;

    TreeNode(T data) {
        this.data = data;
    }

    public T getData() {
        return data;
    }

    public void setLeft(TreeNode<T> left) {
        this.left = left;
    }

    public void setRight(TreeNode<T> right) {
        this.right = right;
    }

    public TreeNode<T> getLeft() {
        return left;
    }

     public TreeNode<T> getRight() {
        return right;
    }


}

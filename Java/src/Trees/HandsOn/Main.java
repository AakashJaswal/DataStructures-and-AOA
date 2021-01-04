package Trees.HandsOn;

import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void print(TreeNode node) {
        System.out.print(node.getData() + " ");
    }


    public static void PreOrderDFS(TreeNode root) {
        if (root == null) return;
        print(root);
        PreOrderDFS(root.getLeft());
        PreOrderDFS(root.getRight());
    }

    public static void InOrderDFS(TreeNode root) {
        if (root == null) return;
        InOrderDFS(root.getLeft());
        print(root);
        InOrderDFS(root.getRight());
    }

    public static void PostOrderDFS(TreeNode root) {
        if (root == null) return;
        PostOrderDFS(root.getLeft());
        PostOrderDFS(root.getRight());
        print(root);
    }


    public static void BFS(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode proc = q.poll();
            print(proc);
            if (proc.getLeft() != null) {
                q.add(proc.getLeft());
            }
            if (proc.getRight() != null) {
                q.add(proc.getRight());
            }

        }
    }

    public static void main(String[] args) {

        TreeNode<Character> a = new TreeNode<>('A');
        TreeNode<Character> b = new TreeNode<>('B');
        TreeNode<Character> c = new TreeNode<>('C');
        TreeNode<Character> d = new TreeNode<>('D');
        TreeNode<Character> e = new TreeNode<>('E');
        TreeNode<Character> f = new TreeNode<>('F');
        TreeNode<Character> g = new TreeNode<>('G');


        a.setLeft(b);
        a.setRight(c);
        b.setRight(e);
        b.setLeft(d);
        c.setLeft(f);
        c.setRight(g);


        BFS(a);
        System.out.println();
        PreOrderDFS(a);
        System.out.println();
        PostOrderDFS(a);
        System.out.println();
        InOrderDFS(a);

    }
}

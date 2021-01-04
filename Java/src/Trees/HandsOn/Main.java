package Trees.HandsOn;

import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void print(TreeNode node) {
        System.out.println(node.getData());
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
        TreeNode<Character> h = new TreeNode<>('H');

        a.setLeft(b);
        a.setRight(c);
        c.setRight(e);
        c.setLeft(d);
        d.setLeft(f);
        d.setRight(h);
        e.setRight(g);

        BFS(a);
    }
}

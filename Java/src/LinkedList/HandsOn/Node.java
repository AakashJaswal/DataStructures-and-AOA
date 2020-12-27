package LinkedList.HandsOn;

public class Node<T extends Comparable<T>> {
    private T data;
    private Node<T> next;

    Node(T data) {
        this.data = data;
    }

    T getData() {
        return data;
    }

    void setNext(Node<T> next) {
        this.next = next;
    }

    Node<T> getNext() {
        return next;
    }

}

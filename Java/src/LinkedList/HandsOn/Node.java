package LinkedList.HandsOn;

public class Node<T extends Comparable<T>> {
    private T data;
    private Node<T> next;

    Node<T> getNext() {
        return next;
    }

    T getData() {
        return data;
    }

    Node(T data) {
        this.data = data;
        setNext(null);
    }

    void setNext(Node<T> next) {
        this.next = next;
    }

}

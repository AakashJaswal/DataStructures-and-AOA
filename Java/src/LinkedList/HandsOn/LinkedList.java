package LinkedList.HandsOn;

public class LinkedList<T extends Comparable<T>> {
    LinkedList() {
    }

    Node<T> head = null;

    void addNode(T data) {
        if (head == null) {
            head = new Node<>(data);
        } else {
            Node curr = head;
            while (curr.getNext() != null) {
                curr = curr.getNext();
            }
            curr.setNext(new Node<T>(data));
        }
    }

    void display() {
        if (head == null) {
            System.out.println("Empty Linked List");
        } else {
            Node curr = head;
            int i = 0;
            while (curr != null) {
                System.out.println(i + " Node is having value: " + curr.getData() + " ");
                curr = curr.getNext();
                i++;
            }

        }
    }
}

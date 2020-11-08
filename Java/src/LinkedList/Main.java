package LinkedList;

class Node<T extends Comparable<T>> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        setNext(null);
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }

    public Node<T> getNext() {
        return next;
    }
}

class LinkedList<T extends Comparable<T>> {
    private Node<T> head = null;

    LinkedList() {

    }

    /**
     * Adds a new node to the Linked List
     * @param data
     */
    void addNode(T data){
        if (head == null){
            head = new Node<T>(data);
        }
        else {
            Node curr = head;
            while(curr.getNext() != null){
                curr = curr.getNext();
            }
            curr.setNext(new Node(data));
        }
    }

    /**
     * Print the Node
     */
    void printNodes(){
        if(head == null){
            System.out.println("LinkedList is empty");
        }
        else {
            Node<T> curr = head;
            int i = 1;
            while (curr != null){
                System.out.println("Value at Node "+i+" is: "+curr.getData().toString());
                curr = curr.getNext();
                i++;
            }
        }
    }


}

public class Main{
    public static void main(String[] args){

        LinkedList<Integer> linkedList = new LinkedList<Integer>();
        linkedList.printNodes();
        linkedList.addNode(2);
        linkedList.addNode(4);
        linkedList.printNodes();
    }
}

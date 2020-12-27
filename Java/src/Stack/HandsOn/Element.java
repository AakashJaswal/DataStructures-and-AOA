package Stack.HandsOn;

public class Element<T> {
    T data;
    Element<T> next;

    Element(T data, Element next) {
        this.data = data;
        this.next = next;
    }

    T getData() {
        return data;
    }

    Element<T> getNext() {
        return next;
    }

}

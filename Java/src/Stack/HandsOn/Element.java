package Stack.HandsOn;

public class Element<T> {
    T data;
    Element<T> next;

    Element(T data, Element next) {
        this.data = data;
        this.next = next;
    }

    Element<T> getNext() {
        return next;
    }

    T getData() {
        return data;
    }
}

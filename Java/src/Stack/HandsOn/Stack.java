package Stack.HandsOn;

public class Stack<T> {
    int size = 0;
    Element<T> top;

    static class SOE extends Exception {
    }

    static class SUE extends Exception {
    }

    void push(T data) throws SOE {
        Element el = new Element(data, top);
        top = el;
        size++;
    }

    T peek() throws SUE {
        if (size == 0) {
            throw new SUE();
        }
        return top.getData();
    }

    T pop() throws SUE {
        if (size == 0) {
            throw new SUE();
        }
        T top_data = top.getData();
        top = top.getNext();
        return top_data;
    }
}

package test;

class Element<T> {
    T data;
    Element<T> next;

    public Element(T data, Element<T> next) {
        this.data = data;
        this.next = next;

    }

    T getData() {
        return data;
    }

    void setNext(Element<T> next) {
        this.next = next;
    }

    Element<T> getNext() {
        return next;
    }
}

class Stack<T> {

    public static class SUE extends Exception {
    }

    Element<T> top;


    int size = 0;

    void push(T data) {

        Element<T> temp = new Element<>(data, top);
        top = temp;
        size++;
    }

    T pop() throws SUE {
        if (size == 0) {
            throw new SUE();
        }
        T re = top.getData();
        top = top.getNext();
        size--;
        return re;
    }
}

public class parantheise {

    public static void main(String[] args) throws Stack.SUE {
        Stack<Character> st = new Stack<>();
        String str = "{{}[][[";
        char[] ch = str.toCharArray();
        for (char c : ch) {
            if (c == '{' || c == '(' || c == '[') {
                st.push(c);
            } else {
                try {
                    char t = st.pop();
                    if (t == '{' && c == '}' || t == '(' && c == ')' || t == '[' && c == ']') continue;
                    else { System.exit(1);}


                } catch (Exception e) {
                    System.out.println("Not balanced");
                    System.exit(1);
                }
            }
        }
        if(st.size > 0)System.out.println("Not Balanced");
        else System.out.println("Balanced");

    }
}

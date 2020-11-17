package Stack.HandsOn;

public class Main {
    public static void main(String[] args) throws Stack.SOE, Stack.SUE{
        Stack<Integer> stack = new Stack<>();

        stack.push(2);
        stack.push(4);
        System.out.println(stack.peek());
        stack.pop();
        System.out.println(stack.peek());
    }
}

import java.util.Stack;
public class stackData{
    public static void main(String[] args)throws Exception{
        Stack<Integer> stack = new Stack<>();
        stack.push(9);
        stack.push(8);
        stack.push(10);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        //System.out.println(stack.pop());// if no element is in the stack it through error

        St n = new St(10);
        n.push(10);
        n.push(9);
        n.push(8);
        n.push(7);
        n.push(6);
        n.push(5);
        n.push(4);
        n.push(3);
        n.push(2);
        n.push(1);
        n.push(0);

        System.out.println(n.pop());
        System.out.println(n.peek());
        System.out.println(n.pop());
        System.out.println(n.peek());

    }
}

class St{
    protected int[] data;
    private static final int DEFAULT_SIZE = 10;

    int ptr = -1;

    public St(){
        this(DEFAULT_SIZE);
    }
    public St(int size){
        this.data = new int[size];
    }
    public boolean push(int item){
        if(isFull()){
            System.out.println("Stack is full");
            return false;
        }
        ptr++;
        data[ptr] = item;
        return true;
    }
    public int pop()throws Exception{
        if(isEmpty()){
            throw new Exception("Cannot pop from an empty Stack!");
        }
        int remove = data[ptr];
        ptr--;
        return remove;
    }
    public int peek() throws Exception{
        if(isEmpty()){
            throw new Exception("Cannot peek from an empty Stack!");
        }
        return data[ptr];
    }
    private boolean isFull(){
        return ptr == data.length-1;
    }
    private boolean isEmpty(){
        return ptr == -1;
    }
}
import java.util.*;
public class QueueData{
    public static void main(String[] args){
        Queue<Integer> qu = new LinkedList<>();
        qu.add(9);
        qu.add(8);
        qu.add(7);
        System.out.println(qu.peek());
        System.out.println(qu.remove());        
        System.out.println(qu.remove());

        Deque<Integer> de = new ArrayDeque<>();
        de.add(10);
        System.out.println(de.peek());

    }
    
}
class CustomQueue{
    private int[] data;
    private static final int DEFAULT_SIZE = 10;
    
}
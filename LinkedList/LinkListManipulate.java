public class LinkListManipulate{
    public static void main(String[] args) {



    }
}

public class LinkL{

    private Node head;
    private Node tail;
    private int size;

    public LinkL(){
        this.size = 0
    }

    public void insert(int val){
        Node node = new Node(val);
        node.next = head;
        head = node;

        if(tail = null){
            tail = head;
        }
        size+=1;

    }



    private class Node{ // every node have  these two things val and Node 
        private int val;
        private Node next;

        public Node(int val){
            this.val = val;

        }
        public Node(int val, Node next){
            this.val = val;
            this.next = next;
        }
    }
}
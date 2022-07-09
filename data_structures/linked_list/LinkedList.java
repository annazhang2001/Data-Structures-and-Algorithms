package data_structures.linked_list;

public class LinkedList {
    Node head;
    public void insert(int data)
    {
        Node node = new Node();
        node.data = data;

        if (head==null){
            head = node;
        }
        else
        {
            Node n = head;
            while (n.next != null){
                n = n.next;
            }
            n.next = node;
        }
    }
    public void show(){
        Node node = head;
        while (node != null){
            System.out.println((node.data));
            node = node.next;
        }
    }
}   

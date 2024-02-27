// Creation Date: 14-06-2020

import java.util.*;

class LinkedList{

    Node head;

    static class Node{
        int data;
        Node next;

        Node(int d){
            data = d;
            next = null; 
        }
    }

    public static void main(String[] args){
        LinkedList llist = new LinkedList();

        llist.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        llist.head.next = second;
        second.next = third;

        llist.printList();
    }

    public void printList(){
        Node n = head;
        while(n != null){
            System.out.print(n.data + " ");
            n = n.next;
        }
    }
  

}
public class TowerOfHanoi {
    public static void towerOfHanoi(int n, char source, char auxiliary, char destination) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + source + " to " + destination);
            return;
        }
        towerOfHanoi(n - 1, source, destination, auxiliary);
        System.out.println("Move disk " + n + " from " + source + " to " + destination);
        towerOfHanoi(n - 1, auxiliary, source, destination);
    }

    public static void main(String[] args) {
        int n = 3;
        towerOfHanoi(n, 'A', 'B', 'C');
    }
}





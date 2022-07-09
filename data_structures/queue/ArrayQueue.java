package data_structures.queue;
import java.util.NoSuchElementException;

import data_structures.linked_list.linkedlists.*;

public class ArrayQueue {
    
    private Employee[] queue;
    private int front;
    // Always pointing to the next available position
    private int back;

    public ArrayQueue(int capacity) {
        queue = new Employee[capacity];
    }

    public void add(Employee employee) {
        if (back == queue.length) {
            Employee[] newArray = new Employee[2 * queue.length];
            System.arraycopy(queue, 0, newArray, 0, queue.length);
        }

        queue[back] = employee;
    }

    public Employee remove() {
        if (size() == 0){
            throw new NoSuchElementException();
        }

        Employee employee = queue[front];
        queue[front] = null;
        front ++;
        // Reset if empty queue
        if (size() == 0){
            front = 0;
            back = 0;
        }
        return employee;
    }

    public Employee peek(){
        if (size() == 0){
            throw new NoSuchElementException();
        }
        return queue[front];
    }

    public int size(){
        return back-front;
    }
    public void printQueue(){
        for (int i = front; i < back; i++){
            System.out.println(queue[i]);
        }
    }
}

package data_structures.stack;
import data_structures.linked_list.linkedlists.*;

public class Main {

    public static void main(String[] args){
        ArrayStack stack = new ArrayStack(10);
        stack.push(new Employee("Jane", "Jones", 123));
        stack.push(new Employee("John", "Jones", 22));
        stack.push(new Employee("Mary", "Smith", 22));
    
        System.out.println(stack.peek());
        stack.printStack();
    }   

    
}

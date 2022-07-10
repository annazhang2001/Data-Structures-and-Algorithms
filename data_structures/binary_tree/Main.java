package data_structures.binary_tree;

public class Main {
    public static void main(String args[]){
        Tree intTree = new Tree();
        intTree.insert(25);
        intTree.insert(20);
        intTree.insert(27);
        intTree.insert(30);
        intTree.insert(29);
        intTree.insert(32);


        System.out.println(intTree.max());

        System.out.println(intTree.min());

        intTree.delete(32);

        intTree.delete(20);

        intTree.traverseInOrder();

    }
}

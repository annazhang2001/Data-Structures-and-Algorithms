package leetcode.medium;

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        
        // Intersection of linked list
        Node p_pointer = p;
        Node q_pointer = q;
        
        while (p_pointer != q_pointer){
            
            if (p_pointer != null){
                p_pointer = p_pointer.parent;
            }
            else {
                p_pointer = q;
            }
            
            if (q_pointer != null){
                q_pointer = q_pointer.parent;
            }
            else {
                q_pointer = p;
            }
            
            
        }
        
        
        return p_pointer;
        
        
        
    }
}
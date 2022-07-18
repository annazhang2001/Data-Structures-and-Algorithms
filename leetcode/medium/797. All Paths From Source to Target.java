package leetcode.medium;

class Solution {
    
    List<List<Integer>> res = new LinkedList<>();
    
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        
        LinkedList<Integer> path = new LinkedList<>();
        traverse(graph, 0, path);
        return res;
    }
    
    public void traverse(int[][]graph, int source, LinkedList<Integer> path){
        
        path.addLast(source);
        
        if (source == graph.length-1){
            res.add(new LinkedList<>(path));
        }
        
        else {
            for (int child: graph[source]){
                traverse(graph, child, path);
            }
            
        }
        
        path.removeLast();
        
    }
        
        
}

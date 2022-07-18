package leetcode.medium;

class Solution {
    
    List<Integer> topOrder = new ArrayList<>();
    int[] states; // 0 means unvisited, 1 means visited, 2 means onPath
    boolean hasCycle = false;
        
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        states = new int[numCourses];
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        
        
            
        for (int i = 0; i < numCourses; i++){
            traverse(graph, i);
        }
    
        if (hasCycle){
            return new int[]{};
        }
        
        int[] res = new int[numCourses];
        for (int i = 0; i < numCourses; i++){
            res[i] = topOrder.get(i);
        }
        
        return res;
    }
    
    public List<Integer>[] buildGraph(int numCourses, int[][] prerequisites){
        
        List<Integer>[] graph = new LinkedList[numCourses];
        
        for (int i = 0; i < numCourses; i++){
            graph[i] = new LinkedList<>();
        }
        
        for (int[] edges: prerequisites){
            int to = edges[0];
            int from = edges[1];
            graph[to].add(from);
        }
        
        return graph;
    }
    
    public void traverse(List<Integer>[]graph, int s){
        
        if (states[s] == 2){
            hasCycle = true;
        }
        if (states[s] == 1 || states[s] == 2){
            return;
        }
        
        states[s] = 2;
        
        for (int t : graph[s]){
            traverse(graph, t);
        }
        
        states[s] = 1;
        topOrder.add(s);
        
    }
        
        
        
        
}
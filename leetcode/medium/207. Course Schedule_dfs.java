package leetcode.medium;

class Solution {
    boolean hasCycle = false;
    boolean[] onPath;
    boolean[] visited;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        
        for (int i = 0; i < numCourses; i++){
        
            traverse(graph, i);
        }
        
        return !hasCycle;
    }
    
    public List<Integer>[] buildGraph(int numCourses, int[][] prereq){
        List<Integer>[] graph = new LinkedList[numCourses];
        
        for (int i = 0; i < numCourses; i++){
            graph[i] = new LinkedList<>();
        }
        
        for (int[] edges : prereq){
            int from = edges[1];
            int to = edges[0];
            
            graph[from].add(to);
        }
        
        return graph;
    }
    
    public void traverse(List<Integer>[] graph, int s){
        // All visited
        
        if (onPath[s]){
            hasCycle = true;
           
        }
        
        if (visited[s] || onPath[s]){
            return;
        }
        
        onPath[s] = true;
        visited[s] = true;
        
        for (int t: graph[s]){
            traverse(graph, t);
        }
        
        onPath[s] = false;
    }
    
    
    
}
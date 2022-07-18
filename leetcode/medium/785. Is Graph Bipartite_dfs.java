package leetcode.medium;

class Solution {
    
    boolean[] visited;
    int[] color;
    boolean bi = true;
    
    public boolean isBipartite(int[][] graph) {
        
        // DFS
        int n = graph.length;
        visited = new boolean[n];
        color = new int[n];
        
        for (int i = 0; i < n; i++){
            if (!visited[i]){
                traverse(i, graph);
            }
        }
        
        return bi;
    }
    
    public void traverse(int s, int[][]graph){
        if (!bi) {
            return;
        }
        
        visited[s] = true;
        
        for (int t : graph[s]){
            if (!visited[t]){
                color[t] = 1 - color[s];
                traverse(t, graph);
            }
            else {
                if (color[s] == color[t]){
                    bi = false;
                    return;
                }
            }
            
        }
        
    }
}
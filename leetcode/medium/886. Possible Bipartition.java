package leetcode.medium;

class Solution {
    
    boolean bi = true;
    boolean[] visited;
    int[] color;
    
    public boolean possibleBipartition(int n, int[][] dislikes) {
        
        // DFS
        visited = new boolean[n + 1];
        color = new int[n + 1];
        
        List<Integer>[] graph = buildGraph(n, dislikes);

        for (int i = 1; i <= n; i++){
            if (!visited[i]){
                traverse(graph, i);
            }
        }
        
        return bi;
    }
    
    public List<Integer>[] buildGraph(int n, int[][] dislikes){
        List<Integer>[] graph = new LinkedList[n + 1];
        
        for (int i = 1; i <= n; i++){
            graph[i] = new LinkedList<>();
        }
        
        for (int[] edge: dislikes){
            int to = edge[0];
            int from = edge[1];
            
            graph[to].add(from);
            graph[from].add(to);
        }
        
        return graph;
    }
    
    public void traverse(List<Integer>[] graph, int s){
        
        if (!bi){
            return;
        }
        
        visited[s] = true;
        for (int t: graph[s]){
            if (!visited[t]){
                color[t] = 1 - color[s];
                traverse(graph, t);
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
package leetcode.medium;

class Solution {
    
    boolean[] visited;
    
    public int countComponents(int n, int[][] edges) {
        
        // DFS
        List<Integer>[] graph = buildGraph(n, edges);
        visited = new boolean[n];
        int counter = 0;
        
        for (int i = 0; i < n; i++){
            
            if (!visited[i]){
                counter++;
                dfs(graph, i);
            }
        }
        
        
        return counter;
    }
    
    public List<Integer>[] buildGraph(int n, int[][] edges){
        
        List<Integer>[] graph = new LinkedList[n];
        
        for (int i = 0; i < n; i++){
            graph[i] = new LinkedList<>();
        }
        
        for (int[] edge: edges){
            int v = edge[0];
            int w = edge[1];
            graph[v].add(w);
            graph[w].add(v);
        }
        
        return graph;
        
    }
    
    public void dfs(List<Integer>[] graph, int v){
        visited[v] = true;
        
        for (int w : graph[v]){
            if (!visited[w]){
                dfs(graph, w);
            }
        }
        
    }
    
    
}
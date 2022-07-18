package leetcode.medium;

class Solution {

    
    public boolean isBipartite(int[][] graph) {
        
        
        boolean bi = true;
        
        // BFS
        int n = graph.length;
        boolean[] visited = new boolean[n];
        int[] color = new int[n];
        
        Deque<Integer> q = new ArrayDeque<Integer>();
        
        for (int i = 0; i < n; i++){
            if (!visited[i]){
                q.add(i);
            }
            
            while (!q.isEmpty()){
                int s = q.poll();
                visited[s] = true;
                for (int t: graph[s]){
                    if (!visited[t]){
                        color[t] = 1-color[s];
                        q.add(t);
                    }
                    else {
                        if (color[t] == color[s]){
                            bi = false;
                        }
                    }
                }
            }
        }
        
        return bi;
        
        
        
    }
    
}
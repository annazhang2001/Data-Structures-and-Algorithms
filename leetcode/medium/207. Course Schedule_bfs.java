package leetcode.medium;

class Solution {
    boolean hasCycle = false;
    boolean[] onPath;
    boolean[] visited;
    
    // BFS
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        
        int[] indegrees = new int[numCourses];
        
        for (int[] edge: prerequisites){
            int to = edge[0];
            int from = edge[1];
            
            indegrees[to] += 1;
            
        }
        
        Deque<Integer> q = new ArrayDeque<>();
        int count = 0;
        for (int i = 0; i < numCourses; i++){
            if (indegrees[i] == 0){
                q.add(i);
            }
        }
        
        while (!q.isEmpty()){
            int s = q.poll();
            count++;
            for (int t: graph[s]){
                indegrees[t]--;
                if (indegrees[t] == 0){
                    q.add(t);
                }
            }
            
        }
        
        return count == numCourses;
        
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
    
    
}
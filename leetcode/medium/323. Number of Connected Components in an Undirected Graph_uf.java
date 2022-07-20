package leetcode.medium;

class Solution {
    
    boolean[] visited;
    
    public int countComponents(int n, int[][] edges) {
        
        // Union Find
        UF uf = new UF(n);
        
        for (int[] edge : edges){
            uf.union(edge[0], edge[1]);
        }
        
        return uf.count();
        
        
    }
    
    // Union Find class
    class UF {
        private int count;
        private int[] parent;
        
        public UF(int n){
            parent = new int[n];
            this.count = n;
            
            for (int i = 0; i < n; i++){
                parent[i] = i;
            }
            
        }
        
        public void union(int p, int q){
            int rootP = find(p);
            int rootQ = find(q);
            
            if (rootP == rootQ){
                return;
            }
            
            parent[rootP] = rootQ;
            count--;
        }
        
        public boolean connected(int p, int q){
            return (find(p) == find(q));
        }
        
        public int find(int x){
            if (parent[x] != x){
                parent[x] = find(parent[x]);
            }
            
            return parent[x];
        }
        
        public int count(){
            return count;
        }
    }
}
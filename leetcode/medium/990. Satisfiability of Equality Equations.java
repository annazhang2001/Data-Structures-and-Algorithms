package leetcode.medium;

class Solution {
    public boolean equationsPossible(String[] equations) {
        
        // Union Find
        UF uf = new UF(26);
        
        for (String eq : equations){
            if (eq.charAt(1) == '='){
                uf.union(eq.charAt(0) - 'a', eq.charAt(3) - 'a');
            }
            
        }
        
        for (String eq : equations){
            if (eq.charAt(1) == '!'){
                if (uf.connected(eq.charAt(0) - 'a', eq.charAt(3) - 'a')){
                    return false;
                }
            }
        }
        
        
        return true;
        
        
    }
    
    class UF {
        private int count;
        private int[] parent;
        
        public UF(int n){
            this.count = n;
            parent = new int[n];
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
        
        public int find(int p){
            if (p != parent[p]){
                parent[p] = find(parent[p]);
            }
            return parent[p];
        }
        
        public int count(){
            return count;
        }
        
        public boolean connected(int p, int q){
            return find(p) == find(q);
        }
        
    }
        
}
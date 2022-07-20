package leetcode.medium;

class Solution {
    int ROWS;
    int COLS;
    
    public void solve(char[][] board) {
        
        // Union Find
        if (board.length == 0){
            return;
        }
        
        int m = board.length;
        int n = board[0].length;
        
        UF uf = new UF(m * n + 1);
        int dummy = m * n;
        
        for (int i = 0; i < m; i++){
            if (board[i][0] == 'O'){
                uf.union(dummy, i * n);
            }
            if (board[i][n-1] == 'O'){
                uf.union(dummy, i * n + (n-1));
            }
            
        }
        
        for (int i = 0; i < n; i++){
            if (board[0][i] == 'O'){
                uf.union(dummy, i);
            }
            if (board[m-1][i] == 'O'){
                uf.union(dummy, n * (m-1) + i);
            }
        }
        
        int[][] d = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        for (int r = 1; r < m-1; r++){
            for (int c = 1; c < n-1; c++){
                if (board[r][c] == 'O'){
                    for (int k = 0; k < 4; k++){
                        int i = r + d[k][0];
                        int j = c + d[k][1];
                        if (board[i][j] == 'O'){
                            uf.union(r * n + c, i * n + j);
                        }
                    }
                }
                
                
            }
        }
        
        
        for (int i = 1; i < m-1; i++){
            for (int j = 1; j < n-1; j++){
                if (board[i][j] == 'O'){
                    if (!uf.connected(dummy, i * n + j)){
                        board[i][j] = 'X';
                    }
                }
            }
        }
        
        
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
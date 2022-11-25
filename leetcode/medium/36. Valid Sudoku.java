class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        int N = 9;
        
        HashSet<Character>[] rows = new HashSet[N];
        HashSet<Character>[] cols = new HashSet[N];
        HashSet<Character>[] boxes = new HashSet[N];
        
        for (int i = 0; i < N; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }
        
        for (int r = 0; r < N; r++) {
            
            for (int c = 0; c < N; c++) {
                
                if (board[r][c] != '.') {
                    if (rows[r].contains(board[r][c])) {
                        return false;
                    } else {
                        rows[r].add(board[r][c]);
                    }
                    if (cols[c].contains(board[r][c])) {
                        return false;
                    } else {
                        cols[c].add(board[r][c]);
                    }
                    
                    int idx = (r / 3) * 3 + c / 3;
                    if (boxes[idx].contains(board[r][c])) {
                        return false;
                    } else {
                        boxes[idx].add(board[r][c]);
                    }
                
            }
        }
    }
    
    return true;
        
    }
        
    
}
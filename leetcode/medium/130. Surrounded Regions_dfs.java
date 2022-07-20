package leetcode.medium;

class Solution {
    int ROWS;
    int COLS;
    
    public void solve(char[][] board) {
        
        // DFS
        ROWS = board.length;
        COLS = board[0].length;
        
        // Mark captured cells
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (board[r][c] == 'O' && (r == ROWS-1 || r == 0) || (c == COLS-1 || c == 0)){
                    capture(r, c, board);
                }
                
            }
        }
        
        // Flip cells
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (board[r][c] == 'T'){
                    board[r][c] = 'O';
                }
                else if (board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
            }
        }
        
        
    }
    
    public void capture(int r, int c, char[][] board){
        if (r == ROWS || c == COLS || r < 0 || c < 0 || board[r][c] == 'X' || board[r][c] == 'T'){
            return;
        }
        
        board[r][c] = 'T';
        
        // UP
        capture(r-1, c, board);
            
        // DOWN
        capture(r+1, c, board);
        
        // LEFT
        capture(r, c-1, board);
            
        // RIGHT
        capture(r, c+1, board);
    }
    
}
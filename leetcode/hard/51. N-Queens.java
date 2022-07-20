package leetcode.hard;

class Solution {
    
    // Without "isValid" optimization
    private int size;
    private List<List<String>> res = new ArrayList<>();
    
    public List<List<String>> solveNQueens(int n) {
        
        size = n;
        char[][] emptyBoard = new char[size][size];
        
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++){
                emptyBoard[i][j] = '.';
            }
        }
        
        backtrack(emptyBoard, 0);
        
        return res;
        
    }
    
    public void backtrack(char[][]state, int row){
        if (row == size){
            List<String> board = createBoard(state);
            res.add(board);
            return;
        }
        
        for (int col = 0; col < size; col++){
            if (!isValid(state, row, col)){
                continue;
            }
            
            state[row][col] = 'Q';
            backtrack(state, row+1);
            state[row][col] = '.';
        }
        
    }
    
    public List<String> createBoard(char[][] state){
        List<String> board = new ArrayList<>();
        for (int row = 0; row < size; row++){
            String curr_row = new String(state[row]);
            board.add(curr_row);
        }
        
        return board;
        
    }
    
    public boolean isValid(char[][] board, int row, int col){
        
        int n = board.length;
        // check col
        for (int i = 0; i <= row; i++){
            if (board[i][col] == 'Q'){
                
                return false;
            }
        }
        
        // check right-up
        for (int i = row-1, j = col+1; i >= 0 && j < n; i--, j++){
            
            if (board[i][j] == 'Q'){
                return false;
            }
        }
        
        // check left-up
        for (int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--){
            
            if (board[i][j] == 'Q'){
                return false;
            }
        }
        
        return true;
    }
    
}

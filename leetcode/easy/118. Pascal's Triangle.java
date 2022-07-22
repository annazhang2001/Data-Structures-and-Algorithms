package leetcode.easy;

class Solution {
    
    List<List<Integer>> res = new ArrayList<>();
    int rows = 0;
    
    public List<List<Integer>> generate(int numRows) {
        rows = numRows;
        generateHelper(1);
        
        return res;
    }
    
    public void generateHelper(int numRows){
        if (numRows > rows){
            return;
        }
        
        List<Integer> row = new ArrayList<>();
        row.add(1);
        
        if (numRows > 1){
            for (int i = 1; i < numRows - 1; i++){
                row.add(res.get(numRows - 2).get(i-1) + res.get(numRows - 2).get(i));
                
            }
            row.add(1);
        }
        
        res.add(row);
        generateHelper(numRows + 1);
        
    }
    
}
package leetcode.easy;

class Solution {
    
    int totalRow = 0;
    
    public List<Integer> getRow(int rowIndex) {
        totalRow = rowIndex;
        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        return generateLR(1, firstRow);
    }
    
    public List<Integer> generateLR(int index, List<Integer> prevRow){
        if (index > totalRow){
            return prevRow;
        }
        List<Integer> myRow = new ArrayList<>();
        myRow.add(1);
        
        for (int i = 1; i < index; i++){
            myRow.add(prevRow.get(i-1) + prevRow.get(i));
        }
        myRow.add(1);
        
        return generateLR(index + 1, myRow);
    }
    
}


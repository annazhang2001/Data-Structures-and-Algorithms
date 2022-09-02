class Solution {
    
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        
        while (i < m - 1) {
            if (target >= matrix[i][0] && target < matrix[i+1][0]) {
                break;
            } else {
                i++;
            }
        }
        
        // Binary search
        int left = 0;
        int right = n - 1;
        
        // 左开右开
        while (left <= right) {
            int mid = (right - left) / 2 + left;
            if (target == matrix[i][mid]) {
                return true;
            } else if (target > matrix[i][mid]) {
                left = mid + 1;
            } else if (target < matrix[i][mid]) {
                right = mid - 1;
            }
        }
        
        
        return false;
        
    
    }
}
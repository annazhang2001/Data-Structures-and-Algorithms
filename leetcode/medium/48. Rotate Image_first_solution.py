class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    
        # Mirror transpose on the other diagonal
        n = len(matrix)
        for i in range(n):
            for j in range(n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = tmp
        
        print(matrix)
        # Reverse
        for col in range(n):
            i = 0
            j = n - 1
            while (i < j):
                tmp = matrix[i][col]
                matrix[i][col] = matrix[j][col]
                matrix[j][col] = tmp
                i += 1
                j -= 1
        
        return matrix
                
                
                
                
                
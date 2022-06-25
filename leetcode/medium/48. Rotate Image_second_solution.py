class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    
        # Mirror Image
        height = len(matrix)
        width = len(matrix[0])
        
        # Swap (i, j) with (j, i)
        for i in range(height):
            for j in range(i + 1, width):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # Left-right reversal
        for row in range(height):
            for col in (range(width/2)):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[row][width-1-col]
                matrix[row][width-1-col] = tmp
                
        
        return matrix
                
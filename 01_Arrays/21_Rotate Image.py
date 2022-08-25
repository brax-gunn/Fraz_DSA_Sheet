class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        N = len(matrix)
        
        # transpose 
        for i in range(N):
            for j in range(i):
                val1 = matrix[i][j]
                val2 = matrix[j][i]
                
                matrix[j][i] = val1
                matrix[i][j] = val2
        
        # reverse
        for i in range(N):
            leftPtr = 0
            rightPtr = N-1
            while leftPtr < rightPtr:    
                matrix[i][leftPtr], matrix[i][rightPtr] = matrix[i][rightPtr], matrix[i][leftPtr]
                leftPtr += 1
                rightPtr -= 1

        return
        
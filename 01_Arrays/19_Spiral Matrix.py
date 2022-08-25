class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        M = len(matrix)
        N = len(matrix[0])
        
        rightBoundary = N-1
        downBoundary = M-1
        leftBoundary = 0
        topBoundary = 0
        
        startX = 0
        startY = 0
        
        res = []
        
        while True:
            
            if (startY < leftBoundary or startY > rightBoundary) or (startX < topBoundary or startX > downBoundary):
                break
            
            # move right
            while startY <= rightBoundary:
                # print( matrix[startX][startY], end = " ")
                res.append( matrix[startX][startY]  )
                startY += 1
            topBoundary += 1
            

            startY -= 1
            startX += 1
            
            if (startY < leftBoundary or startY > rightBoundary) or (startX < topBoundary or startX > downBoundary):
                break
                
            # move down
            while startX <= downBoundary:
                # print( matrix[startX][startY], end = " ")
                res.append( matrix[startX][startY]  )
                startX += 1
            rightBoundary -= 1
            startX -= 1
            startY -= 1
            
            if (startY < leftBoundary or startY > rightBoundary) or (startX < topBoundary or startX > downBoundary):
                break
                
            # move left
            while startY >= leftBoundary:
                # print( matrix[startX][startY], end = " ")
                res.append( matrix[startX][startY]  )
                startY -= 1
            downBoundary -= 1
            startY += 1
            startX -= 1
            
            if (startY < leftBoundary or startY > rightBoundary) or (startX < topBoundary or startX > downBoundary):
                break
                
            # move up
            while startX >= topBoundary:
                # print( matrix[startX][startY], end = " ")
                res.append( matrix[startX][startY]  )
                startX -= 1
            leftBoundary += 1
            startX += 1
            startY += 1
            # print(f'-----{startX,startY, rightBoundary}')
        
        
        return res
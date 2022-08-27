class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        M = len(board)
        N = len(board[0])
        
        newBoard = [ [ board[i][j] for j in range(N) ] for i in range(M) ]
        
        for i in range(M):
            for j in range(N):
                self.__changingLife(i, j, newBoard, M, N, board)
        return
    
    def __changingLife(self, row, col, newBoard, M, N, board):
        if row-1 >= 0 and col >= 0 and row-1 < M and col < N:
            top = newBoard[row-1][col]
        else:
            top = float('inf')
            
        if row-1 >= 0 and col+1 >= 0 and row-1 < M and col+1 < N:
            topRight = newBoard[row-1][col+1]
        else:
            topRight = float('inf')
        
        if row >= 0 and col+1 >= 0 and row < M and col+1 < N:
            right = newBoard[row][col+1]
        else:
            right = float('inf')
        
        if row+1 >= 0 and col+1 >= 0 and row+1 < M and col+1 < N:
            downRight = newBoard[row+1][col+1]
        else:
            downRight = float('inf')
        
        if row+1 >= 0 and col >= 0 and row+1 < M and col < N:
            down = newBoard[row+1][col]
        else:
            down = float('inf')
            
        if row+1 >= 0 and col-1 >= 0 and row+1 < M and col-1 < N:
            downLeft = newBoard[row+1][col-1]
        else:
            downLeft = float('inf')
            
        if row >= 0 and col-1 >= 0 and row < M and col-1 < N:
            left = newBoard[row][col-1]
        else:
            left = float('inf')
        
        if row-1 >= 0 and col-1 >= 0 and row-1 < M and col-1 < N:
            topLeft = newBoard[row-1][col-1]
        else:
            topLeft = float('inf')
        
        countOfAlive = 0
        for neighbor in [top, topRight, right, downRight, down, downLeft, left, topLeft]:
            if neighbor == 1:
                countOfAlive += 1

        # case 1
        if newBoard[row][col] == 1 and countOfAlive < 2:
            board[row][col] = 0
        # case 2
        elif newBoard[row][col] == 1 and (countOfAlive == 2 or countOfAlive == 3):
            board[row][col] = newBoard[row][col]
        # case 3
        elif newBoard[row][col] == 1 and countOfAlive > 3:
            board[row][col] = 0
        # case 4
        elif newBoard[row][col] == 0 and countOfAlive == 3:
            board[row][col] = 1
        
        
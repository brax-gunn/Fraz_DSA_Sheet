class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        
    
        for i in range(M):
            for j in range(N):
                if self.__moveOnBoard(i, j, M, N, board, 0, len(word), "", word, {}):
                    return True

        return False
    
    def __moveOnBoard(self, currentRow, currentCol, M, N, board, currentIndex, targetIndex, currentWord, word, visitedArr):
        
        if currentWord == word:
            return True
        
        
        if currentRow < 0 or currentRow >= M or currentCol < 0 or currentCol >= N:
            return False
        
        if (currentRow, currentCol) in visitedArr:
            return False
        
    
        if len(currentWord) > len(word):
            return False

        
        if board[currentRow][currentCol] != word[currentIndex]:
            return False

        visitedArr[(currentRow, currentCol)] = True

        # move up
        if self.__moveOnBoard(currentRow-1, currentCol, M, N, board, currentIndex+1, targetIndex, currentWord+board[currentRow][currentCol], word, visitedArr):
            return True

        # move right
        if self.__moveOnBoard(currentRow, currentCol+1, M, N, board, currentIndex+1, targetIndex, currentWord+board[currentRow][currentCol], word, visitedArr):
            return True

        # move down
        if self.__moveOnBoard(currentRow+1, currentCol, M, N, board, currentIndex+1, targetIndex, currentWord+board[currentRow][currentCol], word, visitedArr):
            return True

        # move left
        if self.__moveOnBoard(currentRow, currentCol-1, M, N, board, currentIndex+1, targetIndex, currentWord+board[currentRow][currentCol], word, visitedArr):
            return True

        del visitedArr[(currentRow, currentCol)]

        return False
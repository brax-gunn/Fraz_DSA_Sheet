class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        memo = {}
        
        count = 0
        
        for songDuration in time:
            currRem = songDuration % 60
            
            if currRem == 0:
                reqDur = 0
            else:
                reqDur = 60-currRem
            
            if reqDur in memo:
                count += memo[reqDur]
            
            if currRem not in memo:
                memo[currRem] = 1
            else:
                memo[currRem] += 1
        
        return count
        
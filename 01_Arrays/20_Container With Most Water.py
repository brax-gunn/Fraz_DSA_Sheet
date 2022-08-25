class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        N = len(height)
        
        leftPtr = 0
        rightPtr = N-1
        
        maxWaterAmount = 0
        
        while leftPtr < rightPtr:
            
            currentWaterAmount = (rightPtr-leftPtr) * min( height[leftPtr], height[rightPtr] )
            
            maxWaterAmount = max( maxWaterAmount, currentWaterAmount )
            
            if height[leftPtr] <= height[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
        
        
        return maxWaterAmount
        
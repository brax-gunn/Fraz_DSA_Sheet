class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allComb = []
        self.__getAllCombination(0, len(candidates), 0, target, candidates, [], allComb)
        return allComb
    
    def __getAllCombination(self, currentIndex, lastIndex, currentSum, targetSum, candidates, currentComb, allComb):
        
        if currentSum > targetSum:
            return
        
        if currentSum == targetSum:
            allComb.append( currentComb.copy() )
            return
        
        if currentIndex >= lastIndex:
            return
        
        # include current elem
        currentComb.append(candidates[currentIndex])
        self.__getAllCombination(currentIndex, lastIndex, currentSum+candidates[currentIndex], targetSum, candidates, currentComb, allComb)
        currentComb.pop()
        
        # exclude current elem
        self.__getAllCombination(currentIndex+1, lastIndex, currentSum, targetSum, candidates, currentComb, allComb)
        
        return
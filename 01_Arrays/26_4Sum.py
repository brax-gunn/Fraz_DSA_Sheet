class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        N = len(nums)
        
        nums.sort()
        
        res = []
        
        i = 0
        while i <= N-4:
            a = nums[i]
            
            j = i+1
            while j <= N-3:
                b = nums[j]
                
                start = j+1
                end = N-1
                
                while start < end:
                    c = nums[start]
                    d = nums[end]

                    currentSum = a + b + c + d
                    
                    if currentSum < target:
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    elif currentSum > target:
                        end -= 1
                        while end > start and nums[end] == nums[end+1]:
                            end -= 1
                    else:
                        res.append( [a,b,c,d] )
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    
                
                j += 1
                while j <= N-3 and nums[j] == nums[j-1]:
                    j += 1
                
            i += 1
            while i <= N-4 and nums[i] == nums[i-1]:
                i += 1
        
        return res
                
                
        
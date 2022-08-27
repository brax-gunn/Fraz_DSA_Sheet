class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        dp = [ float("inf") for _ in range(N) ]
        dp[N-1] = 0
        
        for i in range(N-2, -1, -1):
            

            end = min(i+nums[i]+1, N)

            minStep = min(dp[i:end])
            
            dp[i] = 1 + minStep

        
                    
        return dp[0]
        
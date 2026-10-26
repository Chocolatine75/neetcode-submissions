class Solution:
    def rob(self, nums: List[int]) -> int:

        def aux(nu):
            n = len(nu)
            if n == 0:
                return 0
            
            if n == 1:
                return nu[0]
            
            dp = [0]*n
            dp[0] = nu[0]
            dp[1] = max(nu[0],nu[1])

            for i in range(2,n):

                dp[i] = max(dp[i-2]+nu[i],dp[i-1])
            return dp[-1]
        
        lenn = len(nums)
        if lenn == 1:
            return nums[0]
        
        return max(aux(nums[:-1]),aux(nums[1:]))
        


        
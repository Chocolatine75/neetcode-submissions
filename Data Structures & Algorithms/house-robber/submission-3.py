class Solution:
    def rob(self, nums: List[int]) -> int:
        ln=len(nums)
        memo = [-1]* ln
        def aux(i):
            if i >= ln:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i]= max(nums[i]+aux(i+2),aux(i+1))
            return memo[i]
        
        return aux(0)
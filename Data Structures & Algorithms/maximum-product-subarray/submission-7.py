class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        MAX =1
        MIN =1
        for n in nums:
            t = MAX *n
            MAX = max(MAX*n,n,MIN*n)
            MIN = min(t,n,MIN*n)
            res = max(res,MAX)
        return res
        
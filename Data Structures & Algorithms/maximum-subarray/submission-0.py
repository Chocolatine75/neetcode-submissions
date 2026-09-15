class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        MAX = 0
        res = nums[0]
        for n in nums:

            MAX = max(n,MAX + n)
            res = max(res,MAX)
        return res
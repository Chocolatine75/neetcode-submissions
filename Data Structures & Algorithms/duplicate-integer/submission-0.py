class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for a in range(1,len(nums)):
            if nums[a-1] == nums[a]:
                return True
        return False
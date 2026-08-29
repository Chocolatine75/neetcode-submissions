class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0

        while high >= low:
            mid = (low + high)//2
            if low == high:
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            


        
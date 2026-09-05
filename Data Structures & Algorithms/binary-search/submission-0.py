class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) -1

        while l<=r:
            
            di = (r+l)//2

            if nums[di] == target:
                return di
            
            if nums[di] < target:

                l = di+1
            else:
                r= di-1
        return -1

        
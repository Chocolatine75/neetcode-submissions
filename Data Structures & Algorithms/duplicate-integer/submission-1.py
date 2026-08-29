class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for a in nums:
            if a in res:
                return True
            res.add(a)
        return False
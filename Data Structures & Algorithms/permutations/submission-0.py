class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)
        def back(path):

            if len(path) == ln:
                res.append(path[:])
            
            for i in nums:
                if i not in path :
                    path.append(i)
                    back(path)
                    path.pop()
        back([])
        return res
        
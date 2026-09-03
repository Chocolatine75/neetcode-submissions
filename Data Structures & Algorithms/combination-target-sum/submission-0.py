class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def back(path):

            if sum(path) == target:
                res.append(path[:])
            
            for i in nums:
                if path!= [] and i < path[-1]:
                    continue
                path.append(i)
                if sum(path) <= target:
                    back(path)
                path.pop()
        back([])
        return res

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(path):
            if path not in res:
                res.append(path[:])
            
            for i in nums:
                if path != [] and i < path[-1]:
                    continue
                if i not in path :
                    path.append(i)
                    back(path)
                    path.pop()
        back([])
        return res

        
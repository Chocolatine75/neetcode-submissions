class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ln = len(candidates)
        candidates.sort()
        def back(path,index):
            s = sum(path)
            if s<= target:
                if s == target:
                    res.append(path[:])
                for i in range(index,ln):
                    if i>index and candidates[i]== candidates[i-1]:
                        continue
                    path.append(candidates[i])
                    back(path,i+1)
                    path.pop()
        back([],0)
        return res

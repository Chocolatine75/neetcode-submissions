class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)
        nums.sort()
        def back(path,index):
            
            if path not in res:
                res.append(path[:])
            
            for i in range(index,ln):
                if i >0 and nums[i]< nums[i-1]:
                    continue
                path.append(nums[i])
                back(path,i+1)
                path.pop()
        
        back([],0)
        return res
        
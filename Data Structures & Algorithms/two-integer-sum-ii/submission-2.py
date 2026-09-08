class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ln  = len(numbers)
        l,r = 0,ln-1

        while l<r:

            sumlr = numbers[l] +numbers[r]

            if sumlr > target:
                r -=1
            
            elif sumlr< target:
                l+=1
            else:
                return [l+1,r+1]
        
        return []
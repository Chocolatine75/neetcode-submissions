class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix)-1
        while l <= r:

            t= (l+r)//2

            if target in matrix[t]:
                return True
            
            elif matrix[t][-1] < target:
                l = t+1
            elif matrix[t][0] > target:
                r =t-1
            else:
                return False 
        
        return False
    

        


        
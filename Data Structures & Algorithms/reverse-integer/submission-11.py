class Solution:
    def reverse(self, x: int) -> int:
        
        MAX = 2**31 -1
        MIN = (-2)**31
        res = 0
        sign = False

        if  MIN>=x or x>=MAX:
            return 0
        if x<0:
            sign = True
            x = -x
        
        while x>0:
            if  MIN>=res or res>=MAX:
                return 0
            res += x%10
            res*=10
            x = x//10
        

        

        if sign :
            return -res//10
        return res//10
        
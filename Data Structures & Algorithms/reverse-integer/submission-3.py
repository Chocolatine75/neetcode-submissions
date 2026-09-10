class Solution:

    def reverse(self, x: int) -> int:
        res = 0
        sign = False
        if x<0:
            sign = True
            x = -x
        while x>0:
            res += x%10
            res*=10
            x= x//10
        res =res//10
        if sign:
            res = -res
        if -2**31 > res or res > 2**31 - 1:
                return 0
      
        return res


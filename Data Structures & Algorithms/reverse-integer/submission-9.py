class Solution:

    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        
        sign = False
        if x<0:
            sign = True
            x = -x
        res = x%10
        x =x//10
        while x>0:
            if res > MAX/10 :
                return 0
            
            if res == MAX/10 and x > MAX%10:
                return 0
            
            res =(res*10)+ x%10
            x = x//10
        
       
        if sign:
            res = -res
        
        return res
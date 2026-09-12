class Solution:
    def countSubstrings(self, s: str) -> int:

        ls = len(s)
        res = 0
        dp = [[False]*ls for _ in range(ls)]
        for i in range(ls- 1, -1, -1):
            for j in range(i,ls):

                if s[i]== s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res+= 1
        return res





            
        
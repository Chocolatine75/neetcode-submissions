class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(n):

            if n == 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            res = 1e9
            for coin in coins:

                if n-coin >=0:
                    res = min(res,1+dfs(n-coin))

            memo[n] =res  
            return res
        
        res = dfs(amount)
        if res ==1e9:
            return -1
        return res
        

        
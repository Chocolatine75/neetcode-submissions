class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1]*(amount+1)
        dp[0] = 0
        n = len(coins)

        for i in range(1,amount+1):
            for j in range(n):
                if i-coins[j]>=0:
                    dp[i] = min(dp[i],1+dp[i-coins[j]])
        
        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1


        
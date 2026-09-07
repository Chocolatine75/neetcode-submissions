class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lc =len(cost)
        memo = [-1] *lc

        def dfs(i):

            if i>= lc:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] +min(dfs(i+1),dfs(i+2))
            return memo[i]
        
        return min(dfs(0),dfs(1))

            
        



        
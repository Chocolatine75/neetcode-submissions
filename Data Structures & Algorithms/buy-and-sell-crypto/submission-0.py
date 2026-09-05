class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minu = prices[0]
        maxi = 0
        for s in prices:
            maxi = max(maxi,s -minu)
            minu = min(minu,s)
        return  maxi
        



        
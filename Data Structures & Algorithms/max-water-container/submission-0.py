class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_height = min(heights[i],heights[j])
                pool_size=max_height*(j-i)
                if pool_size >best:
                    best = pool_size
        return best


        
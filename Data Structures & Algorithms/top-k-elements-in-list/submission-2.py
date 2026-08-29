class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for n in nums:
            s[n] =  1+ s.get(n,0)
        
        tri = sorted(s.keys(),key=lambda x:s[x],reverse=True)
        return tri[:k]
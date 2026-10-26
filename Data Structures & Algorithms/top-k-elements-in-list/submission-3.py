class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:

            if n not in freq:
                freq[n] = 1
            else:
                freq[n]+=1
        
        res = sorted(freq.items(),key= lambda x: x[1],reverse=True)
        result = []
        for j in range(k):
            result.append(res[j][0])
        return result
    


        
        
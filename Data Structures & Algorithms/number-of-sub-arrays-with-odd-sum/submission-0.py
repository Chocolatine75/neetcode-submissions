class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 +7

        even_count = 1
        odd_count = 0
        curr = 0
        result = 0
        for num in arr:
            curr+= num
            
            if curr % 2 == 1:
                result += even_count
                odd_count+=1
            else:
                result += odd_count
                even_count +=1
        return result %mod



        
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)  
        res = ""

        for i in range(len(s)):
            if s[i] in t_count:
                t2 = t_count.copy()
                r = ""
                length = i
                while length < len(s) and any(v > 0 for v in t2.values()):
                    if s[length] in t2:
                        t2[s[length]] -= 1
                    r += s[length]
                    length += 1
                if all(v <= 0 for v in t2.values()) and (len(r) < len(res) or len(res) == 0):
                    res = r

        return res


        
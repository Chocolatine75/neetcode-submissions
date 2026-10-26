class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        length = len(strs)
        histo = {}
        for s  in strs:
            key = "".join(sorted(s))
            if key not in histo:
                histo[key] = []
            histo[key].append(s)
        
        return list(histo.values())


        
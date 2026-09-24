class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        output = []
        
        for i in strs:
            s = "".join( sorted(i))
            if s not in d :
                d[s] = [i]  
            elif s in d:
                d[s].append(i)
        return list(d.values())
            
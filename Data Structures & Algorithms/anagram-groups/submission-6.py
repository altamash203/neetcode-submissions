class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        output = []
        count =0
        for i in strs:
            s = "".join( sorted(i))
            if s not in d :
                d[s] = count
                count +=1
                output.append([i])
            elif s in d:
                output[d[s]].append(i)
        return output
            
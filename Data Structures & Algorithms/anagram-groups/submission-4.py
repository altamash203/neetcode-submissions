class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output =[]
        for i in strs:
            s = ''.join(sorted(i))
            if s not in seen :
                seen[s] = [i]
            else:
                seen[s].append(i)
        for i in seen.values():
            output.append(i)
        return output



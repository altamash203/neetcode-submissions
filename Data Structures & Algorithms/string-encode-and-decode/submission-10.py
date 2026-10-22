class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for i in strs :
            l = len(i)
            output.extend(f"{l}#{i}")
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        last = 0
        output = []
        l = len(s)
        i = 0
        while i < l :
            if s[i] == "#":
                num = int(s[last:i])
                output.append(s[i+1 : i+num+1])
                last =i+num+1
                i = last +1
            else :
                i+=1
        return output



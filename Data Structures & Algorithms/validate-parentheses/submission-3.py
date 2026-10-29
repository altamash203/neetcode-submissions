class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(","]":"[","}":"{"}
        stack = []

        for i in s :
            if i  not in d : 
                stack.append(i)
            elif  stack  and  stack[-1] == d[i]:
                stack.pop()
                
            else:
                return False
        if stack:
            return False
        return True
                  

            
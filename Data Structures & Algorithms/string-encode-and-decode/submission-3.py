class Solution:
    

    def encode(self, strs: List[str]) -> str:
        if not strs  :
            return ""
        elif strs ==[""] :
            return " "
        encoded = "*-*".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == " ":
            return [""]
        decoded = s.split("*-*")
        return decoded
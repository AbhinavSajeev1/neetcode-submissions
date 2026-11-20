class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS, hashmapT = {}, {}

        for char in s:
            hashmapS[char] = 1 + hashmapS.get(char,0)
        
        for char in t:
            hashmapT[char] = 1 + hashmapT.get(char,0)

        return hashmapS == hashmapT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chrs = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in chrs:
                chrs[c] +=1
            else:
                chrs[c] = 1
        for c in t:
            if c not in chrs or chrs[c] == 0:
                return False
            chrs[c] -= 1
        return True
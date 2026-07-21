class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        while len(s) != 1:
            if t.find(s[0]) == -1:
                return False
            else:
                idx = t.find(s[0])
                s = s[1:]
                t = t[:idx] + t[idx + 1:]
        if s==t:
            return True
        return False

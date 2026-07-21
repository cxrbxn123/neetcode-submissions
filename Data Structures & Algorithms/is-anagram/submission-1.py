class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = "".join(sorted(s))
        ts = "".join(sorted(t))
        if ss == ts:
            return True
        return False
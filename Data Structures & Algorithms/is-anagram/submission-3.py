class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chrs = [0]*26
        for i in range(len(s)):
            chrs[ord(s[i]) - ord('a')] +=1
            chrs[ord(t[i]) - ord('a')] -=1
        return chrs == [0]*26
            
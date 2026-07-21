class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrs = {}
        left = 0
        maxl = 0
        for i,c in enumerate(s):
            
            if c not in chrs:
                chrs[c] = i
                
            else:
                if chrs[c] >= left:
                    left = chrs[c] +1
                chrs[c] = i
            if maxl< i-left +1:
                maxl = i-left +1

        return maxl

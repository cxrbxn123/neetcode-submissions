class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxc = 1
        t = ""
        s = s + s[0]
        for i in s:
            if i in t:
                if len(t) > maxc:
                    maxc = len(t)

                while i in t:
                    t = t[1:]

                t = t + i
            else:
                if len(t) > maxc:
                    maxc = len(t)
                t = t + i
        return maxc



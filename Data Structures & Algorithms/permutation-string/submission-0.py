class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        s = "".join(sorted(s1))
        cur = s2[:l]
        s2 = s2[l:]
        if s == ("".join(sorted(cur))):
            return True
        for v in s2:
            cur = cur[1:]+v
            if s == ("".join(sorted(cur))):
                return True
        
        return False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return s == t
        elif len(s) == 0:
            return True
        elif len(s) > len(t):
            return False
        needed = deque()
        for c in s:
            needed.append(c)
        for c in t:
            if not needed:
                return True
            if c == needed[0]:
                needed.popleft()
                
        return not needed
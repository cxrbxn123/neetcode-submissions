class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in pairs:
                if not stk or stk.pop() != pairs[c]:
                    return False
            else:
                stk.append(c)

        return not stk
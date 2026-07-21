class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        while len(s) >1:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]
        return True
        
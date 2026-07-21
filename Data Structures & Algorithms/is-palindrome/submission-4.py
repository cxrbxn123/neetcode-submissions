class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        while len(s2) >1:
            if s2[0] != s2[-1]:
                return False
            s2 = s2[1:-1]
        return True
        
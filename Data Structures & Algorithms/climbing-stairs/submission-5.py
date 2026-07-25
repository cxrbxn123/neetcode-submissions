class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        d1 = 1
        d2 = 2
        for i in range(n-2):
            temp = d2
            d2 = d2+d1
            d1 = temp
        return d2
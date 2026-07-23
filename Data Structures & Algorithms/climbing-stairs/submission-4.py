class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        dp1= 1
        dp2 = 1
        
        for i in range(n-1):
            temp = dp2
            dp2 = dp2+dp1
            dp1 = temp
        return dp2
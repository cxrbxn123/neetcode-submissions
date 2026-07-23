class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp1= 1
        dp2 = 2
        
        for i in range(n-2):
            temp = dp2
            dp2 = dp2+dp1
            dp1 = temp
        return dp2
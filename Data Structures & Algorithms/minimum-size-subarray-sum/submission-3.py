class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        t=0
        window = []
        l = 0
        minl = 0
        for n in nums:
            
            window.append(n)
            l +=1
            t +=n
            if t >= target:
                while t>=target:
                    if l<minl or minl == 0:
                        minl = l
                    t -= window.pop(0)
                    l -= 1
        return minl
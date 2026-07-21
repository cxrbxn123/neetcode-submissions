class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ma = {}
        for x in nums:
            if ma.get(x,-1) == -1:
                ma[x] = 1
            else:
                del ma[x]
        return(next(iter(ma.keys())))

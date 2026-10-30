class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        total = 1
        n0 = []
        for i,n in enumerate(nums):
            if n != 0:
                total *= n
            else:
                if len(n0) <1:
                    n0.append(i)
                else:
                    return [0]*len(nums)
        if len(n0) >0: 
            out = [0] * len(nums)
            out[n0[0]] = total
            return out
        out = [total] * len(nums)
        for i,n in enumerate(nums):
            out[i] = out[i]//n
        return out

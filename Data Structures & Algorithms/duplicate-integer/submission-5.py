class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashs = {}
        for n in nums:
            if n in hashs:
                return True
            else:
                hashs[n] = 1

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashs = set()
        for n in nums:
            if n in hashs:
                return True
            hashs.add(n)
                

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past = set()
        for n in nums:
            if n in past:
                return True
            else:
                past.add(n)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            cur = nums[i]
            for j in nums[i+1:len(nums)]:
                if cur == j:
                    return True
        return False

        
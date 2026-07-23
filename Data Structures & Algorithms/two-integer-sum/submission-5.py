class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countr = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in countr:
                return [countr[other],i]
            countr[nums[i]] = i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        hashs = {}
        for n in nums:
            
            needs = target-n
            if needs in hashs:
                return [hashs[needs], i]
            hashs[n] = i
            i += 1
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        data = {}
        maxl = 1
        curl = 1
        for n in nums:
            data[n] = 1
        sorted_data = list(dict(sorted(data.items())).keys())
        prev = sorted_data[0]
        for n in sorted_data[1:]:
            if prev == n-1:
                curl+=1
                if curl > maxl:
                    maxl = curl
            else:
                curl = 1
            prev = n
        return maxl
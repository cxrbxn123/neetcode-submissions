class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashs = {}
        for n in nums:
            if  n in hashs:
                hashs[n] += 1
            else: 
                hashs[n] = 1
        sorts = sorted(hashs, key=hashs.get, reverse=True)
        return sorts[0:k]
        
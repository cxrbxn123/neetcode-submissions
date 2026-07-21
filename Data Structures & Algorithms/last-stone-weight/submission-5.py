class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*-1
        minHeap = stones
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            new = abs(heapq.heappop(minHeap)- heapq.heappop(minHeap)) * -1
            heapq.heappush(minHeap, new)
        if not minHeap:
            return 0
        return (heapq.heappop(minHeap)*-1)
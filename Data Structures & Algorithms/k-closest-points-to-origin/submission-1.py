class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = defaultdict(list)
        heapDist = []
        output = []
        big = 0
        i= 1
        for point in points:
            d = math.sqrt(point[0]**2+point[1]**2)
            if i<=k:
                heapq.heappush(heapDist,d)
                distances[d].append(point)
            elif d< big:
                heapq.heappush(heapDist,d)
                distances[d].append(point)
        for i in range(k):
            d = heapq.heappop(heapDist)
            output.append(distances[d].pop())
        return output
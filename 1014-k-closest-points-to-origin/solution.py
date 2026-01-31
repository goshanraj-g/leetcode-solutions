class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        heap = []
        
        for point in points:
            dist = point[0]**2 + point[1]**2 
            heap.append((dist, point))
        
        heapq.heapify(heap)
        
        for _ in range(k):
            dist, coordinates = heapq.heappop(heap)
            res.append(coordinates)
            
        return res

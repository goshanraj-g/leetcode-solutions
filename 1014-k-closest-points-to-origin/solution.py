import math

class Solution(object):
    def kClosest(self, points, k):
        res = []
        vals = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0]**2) + (points[i][1]**2))
            vals.append([dist,i])
        heapq.heapify(vals)

        while k > 0:
            if vals:
                dist, idx = heapq.heappop(vals)
                res.append(points[idx])
                k -= 1
        return res

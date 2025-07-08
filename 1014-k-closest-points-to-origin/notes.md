# **Approach**
- Initialize a minHeap array
- Calculate the distance of each point from origin with the formula, sqrt((x1 - x2)^2 + (y1 - y2)^2)
- Add a list of the distance, x and y to the minHeap array
- Initialize a min heap (heapq.heapify(minHeap)
- For k iterations, pop the top value in the heap
- Return an array with the k values

# **Solution**
<pre>
Class Solution(object):
  def kClosest(self, points, k):
    minHeap = []
    for x, y in points:
      dist = (x ** 2) + (y ** 2)
      minHeap.append([dist, x, y])
    heapq.heapify(minHeap)

    res = []
    while k > 0:
      dist, x, y = heapq.heappop(minHeap)
      res.append([x, y])
      k -= 1
  return res
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n + klog n)**
**Space Complexity: O(n)**

## **Key Ideas**
This is a simple **min-heap** problem

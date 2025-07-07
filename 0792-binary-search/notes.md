# **Approach**
- Incorperate a simple binary search algorithm to find the index of the target

# **Solution**
<pre>
class Solution(object):
  def binarySearch(self, nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
      mid = (l+r) // 2
      if nums[mid] > target:
        r = mid - 1
      elif nums[mid] < target:
        l = mid + 1
      else:
        return mid
    return -1
</pre>

## **Time and Space Complexity**
**Time Complexity: O(log n), where n is the length of the input array**
**Space Complexity: O(1), no new allocations of memory, there are only lookups**

## **Key Ideas**
This is a simple **Binary Search** problem

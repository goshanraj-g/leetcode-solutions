# **Approach**
- Initialize a left and right pointer at indices 0, 1 to allow us to calculate profits
- Set a profit variable at 0 as this will be updated every time there is a profit higher than this value
- Set a loop going as long as the right pointer does not end up out of bounds
- If the price at the right pointer is greater or equal to the value of the left pointer, update the profit by calculating the max between the difference and the previous profit
- Shift the right pointer by 1
- If this condition is not true, then left the left pointer by 1
- At the end, return profit 

# **Solution**
<pre>
class Solution(object):
  def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1
    profit = 0
    while (r < len (prices)):
      if (prices[r] >= prices[l]):
        profit = max(prices[r]-prices[l], profit):
        r += 1
      else:
        l += 1
    return profit
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n), where n is the length of the input**
**Space Complexity: O(1), there are no new allocations of memory we are using O(1) lookups**

## **Key Ideas**
This is a simple **Two Pointers** problem

# **Approach**
- We want to be able to find the start of a sequence, and keep adding one to find the longest consecutive sequence
- Intialize a set to avoid looping through duplicates, and initialize a result variable
- Loop through the set, and when the beginning of a sequence is detected, initialize the length to 1
- Keep looping through and while the next number is in the set, increment the length by 1
- Return the length of the longest consecutive subsequence by keeping track of it with max()

# **Solution**
<pre>
class Solution(object):
  def longestConsecutive(self, nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
      if (n-1) in numSet:
        length = 1
        while (n + length) in numSet:
          length += 1
        longest = max(longest, length)
      return longest
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n), where n is the length of the input array**
**Space Complexity: O(n), since you are initializing a new set**

## **Key Ideas**
This is a simple **Set** problem

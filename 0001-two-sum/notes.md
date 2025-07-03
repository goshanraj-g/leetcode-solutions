# **Approach**
- Initialize a hashmap to store previous pairs of values and indices
- Loop over each number, and calculate the difference with the target and current number
- Check if the difference is in the hashmap, if not store the key and value
- Return the two indexes at the end when found

# **Solution**
<pre>
Class Solution(object):
  def twoSum(self, nums, target):
    stored_values = {}
    for num in range(len(nums)):
      difference = target - nums[num]
      if difference in stored_values:
        return [stored_values[difference], num]
      stored_values[nums[num]] = num
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n)**
**Space Complexity: O(n)**

## **Key Ideas**
This is a simple **hashmap for complement lookup** problem

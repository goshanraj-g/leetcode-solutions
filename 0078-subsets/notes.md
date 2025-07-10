# **Approach**
- Define a solution array and a result array, where the solution array will hold an outcome at a time and result will hold all possible outcomes
- Define a recursive backtracking function which takes in an index
- For the base case, if the index passed in reaches the boundary of the length of nums, append the current solution to the result array
- For the recursive cases, simulate one DFS to not add any new elements, and one DFS to add the current index element
- For the second case, make sure to pop after as this will ensure that you will generate more unique outcomes
- Once the recursive function is complete, run it at the index of 0, and then return the result

# **Solution**
<pre>
class Solution(object):
  def subsets(self, nums):
    res, sol = [], []
    def dfs(i):
      if i == len(nums):
        res.append(sol[:])
        return
      dfs(i+1)
      sol.append(nums[i])
      dfs(i+1)
      sol.pop()
    dfs(0)
    return res
</pre>

## **Time and Space Complexity**
**Time Complexity: O(2^n)**
**Space Complexity: O(n), where n is the depth of the recursive call stack**

## **Key Ideas**
- This is a simple **backtracking** problem

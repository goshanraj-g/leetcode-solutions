# **Approach**
- Create a helper function which can strip out capitals, lowercase and special characters
- Create a pointer at the leftmost and rightmost index
- Initialize a loop as long as the left value is less than right index to avoid an out of bounds error
- Every iteration should check if the character is alphanumeric, and if not, shift the appropriate index to avoid it
- If the character on the left does not match the character on the right, return false
- If the previous condition is not met, shift the left pointer up 1, and the right pointer down 1
- Return True at the end

# **Solution**
<pre>
class Solution(object):
  def isPalindrome(self, s):
    l, r = 0, len(s) - 1
    while l < r:
      while l < r and not self.isAlphaNum(s[l]):
        l+=1
      while l < r and not self.isAlphaNum(s[r]):
        r-=1
      if s[l].lower() != s[r].lower():
        return False
      l, r = l + 1, r - 1
    return True

  def isAlphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n), where n is the length of the input string**
**Space Complexity: O(1)**

## **Key Ideas**
This is a simple **Two Pointers** problem

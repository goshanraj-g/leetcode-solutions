# **Approach**
- Create a hashmap for each character for both strings
- Compare both arrays and return True if they are equal, false if not

# **Solution**
<pre>
class Solution(object):
  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    sDict = {}
    tDict = {}
    for char in s:
      sDict[char] = sDict.get(char, 0) + 1
    for char in t:
      tDict[char] = tDict.get(char, 0) + 1
  return sDict == tDict
      

</pre>

## **Time and Space Complexity**
**Time Complexity: O(n)**
**Space Complexity: O(n)**

## **Key Ideas**
- This is a simple **hashmap frequency comparison** problem

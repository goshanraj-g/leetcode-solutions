# **Approach**
- Initialize a hashmap with keys being the closed bracket and values being the open bracket. Initialize an empty stack
- Loop through each character in the string, and if a character is in the keys of the mapping, check if the stack exists, and if the last element in the stack is equal to it's appropriate mapping in the hashmap
- Once checked, if it returns true, pop from the stack, otherwise return false
- When looping through, if the character is not in the mapping, then append it to the stack
- Lastly, once the loop is finished executing, check if the stack is empty. If it is, return True, else return False

# **Solution**
<pre>
class Solution(object):
  def isValid(self, s:str) -> bool:
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
      if char in mapping:
        if stack and stack[-1] == mapping[char]:
          stack.pop()
        else:
          return False
      else:
        stack.append(char)
    if not stack:
      return True
    return False
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n)**
**Space Complexity: O(n), where n is the length of the input string**

## **Key Ideas**
This is a simple **hashmap and stack problem**

# **Approach**
- Check the base case if the tree is empty
- Swap the right and left root nodes
- Recurse down the tree and keep swapping the left and right children

# **Solution**
<pre>
class Solution(object):
  def invertTree(self, root):
    if not root:
      return None

    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    self.invertTree(root.left)
    self.invertTree(root.right)
</pre>

## **Time and Space Complexity**
**Time Complexity: O(n), as every node is only visited once**
**Space Complexity: O(h), where h is the height of the binary tree**

## **Key Ideas**
This is a simple **Binary Tree** Problem

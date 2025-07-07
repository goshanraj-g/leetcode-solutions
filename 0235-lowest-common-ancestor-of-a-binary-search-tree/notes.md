# **Approach**
- We want to be able to find the lowest common ancestor of a BST, given two nodes p and q
- LCA -> The lowest node between two nodes p and q
- Perform a recursive depth-first search (DFS) on the BST, and use conditional statements to check if a node is in between the values of p, and q
- If they are in between return the root, if the values are greater than the root, perform a recursive DFS on the right subtree, otherwise perform a recursive DFS on the left subtree
- Ensure to include a base case to avoid infinite recursion

# **Recursive Solution**
<pre>
class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    def dfs(root):
      if not root:
        return None
      if p.val > root.val and q.val > root.val:
        return dfs(root.right)
      elif p.val < root.val and q.val < root.val:
        return dfs(root.left)
      else:
        return root
    return dfs(root)
</pre>

# **Iterative Solution**
<pre>
class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    cur = root
    while cur:
      if p.val > cur.val and q.val > cur.val:
        cur = cur.right
      elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
      else:
        return cur
</pre>

## **Time and Space Complexity for Recursive Solution**
**Time Complexity: O(log n), where n is the length of the binary tree**
**Space Complexity: O(h), where h is the height of the binary tree**

## **Time and Space Complexity for Iterative Solution**
**Time Complexity: O(log n), where n is the length of the binary tree**
**Space Complexity: O(1)**

## **Key Ideas**
This is a simple **depth-first search binary tree** problem

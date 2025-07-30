# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # going to be  DFS, where you go down each path, and determine if it's a good node, and add 1
        def dfs(root, cur_max):
            if root is None:
                return 0
            if root.val >= cur_max:
                count = 1
            else:
                count = 0
            cur_max = max(cur_max, root.val)
            right = dfs(root.right, cur_max)
            left = dfs(root.left, cur_max)
            return count + right + left
        return dfs(root, root.val)


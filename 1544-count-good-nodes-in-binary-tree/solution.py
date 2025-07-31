# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if not node:
                return 0
            if node.val >= cur_max:
                count = 1
                cur_max = node.val
            else:
                count = 0
            left = dfs(node.left, cur_max)
            right = dfs(node.right, cur_max)
            return count + left + right
        return dfs(root, root.val)

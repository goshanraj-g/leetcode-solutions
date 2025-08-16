# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pot(node):
            if node is None:
                return
            res.append(node.val)
            pot(node.left)
            pot(node.right)
        pot(root)
        return res
        

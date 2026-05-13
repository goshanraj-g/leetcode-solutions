# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def checkBSTProp(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return checkBSTProp(node.left, low, node.val) and \
                    checkBSTProp(node.right, node.val, high)

        return checkBSTProp(root, float("-inf"), float('inf'))

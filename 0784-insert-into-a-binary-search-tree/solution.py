# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if greater than node.val, traverse to right, if not left
        # while node.val exists, traverse to right if greater, or left if less
        # when exitted out of the loop, add it to the left or right
        if not root:
            return TreeNode(val)

        def traverse(node):
            while node:
                if val > node.val:
                    if node.right:
                        node = node.right
                    else:
                        break
                elif val < node.val:
                    if node.left:
                        node = node.left
                    else:
                        break
            if val > node.val:
                node.right = TreeNode(val)
            else:
                node.left = TreeNode(val)
        traverse(root)
        return root
        

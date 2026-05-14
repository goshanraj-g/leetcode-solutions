# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        # we can just do this with in order traversal -> returns minimum
        # decrement k as we go long
        # dfs stack sln

        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()

            k -= 1
            if k == 0:
                return cur.val

            cur = cur.right
        

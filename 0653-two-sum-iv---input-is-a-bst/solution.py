# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        q = deque([root])
        num_set = set()
        while q:
            node = q.popleft()
            if (k - node.val) in num_set:
                return True
            else:
                num_set.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        

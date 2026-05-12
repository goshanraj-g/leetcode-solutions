# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        
        while q:
            q_len = len(q)
            cur_level = []
            for i in range(q_len):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur_level)
        return res


        #traversal of a binary tree, level order
        # this is going to be BFS
        

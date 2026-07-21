# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def comparison(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                if not p and not q:
                    return True
                return False
            if p.val != q.val:
                return False
            return(comparison(p.left, q.left) and comparison(p.right, q.right))
        return comparison(p,q)
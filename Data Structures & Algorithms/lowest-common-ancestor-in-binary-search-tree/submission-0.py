# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start with brute force:
        # brute force would be to iterate through the entire tree, and find p and q
        larger_val = max(p.val,q.val)
        smaller_val = min(p.val,q.val)
        while root:
            cur = root.val
            if smaller_val <= cur <= larger_val:
                return root
            elif larger_val < cur:
                root = root.left
            else:
                root = root.right

        return root
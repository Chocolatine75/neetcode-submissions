# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxi =0
        def dfs(root):
            nonlocal maxi

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            diam = left+right
            maxi = max(maxi,diam)

            return 1+ max(left,right)

        dfs(root)
        return maxi      

        
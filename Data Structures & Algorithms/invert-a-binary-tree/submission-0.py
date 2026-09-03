# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None
        newtree = TreeNode()
        def dfs(r,new):
            new.val = r.val
            
            if r.left != None:
                new.right = TreeNode()
                dfs(r.left,new.right)
            
            if r.right != None:
                new.left = TreeNode()
                dfs(r.right,new.left)
        
        dfs(root,newtree)
        return newtree

        
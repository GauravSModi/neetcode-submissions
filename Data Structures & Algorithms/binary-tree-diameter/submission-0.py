# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # First int = depth
    # Second int = diameter
    def diameterHelper(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return 0, 0

        depthLeft, depthRight, diameterLeft, diameterRight = 0, 0, 0, 0
        
        if root.left:
            depthLeft, diameterLeft = self.diameterHelper(root.left)
            depthLeft += 1
        if root.right:
            depthRight, diameterRight = self.diameterHelper(root.right)
            depthRight += 1

        return max(depthLeft, depthRight), max(depthLeft+depthRight, diameterLeft, diameterRight)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.diameterHelper(root)
        return diameter
        
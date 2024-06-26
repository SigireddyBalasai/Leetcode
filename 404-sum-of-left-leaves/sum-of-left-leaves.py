# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return f(root)

def f(root, isLeft=False):
    if not root: return 0
    if not root.left and not root.right and isLeft: return root.val
    return f(root.left, True)+f(root.right, False)    
        
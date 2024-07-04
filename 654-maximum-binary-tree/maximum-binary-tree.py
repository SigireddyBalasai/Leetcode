# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
      return self.construct_tree(nums)

    def construct_tree(self,nums):
        if len(nums) == 0:
            return None
        root,left,right=self.split(nums)
        if len(left) != 0:
            left= self.construct_tree(left)
        else:
            left = None    
        if len(right) != None:
            right=self.construct_tree(right)
        else:
            right = None
        root=TreeNode(root,left,right)
        return root
    def split(self,nums):
            split_index=nums.index(max(nums))
            root=nums[split_index]
            left=(nums[0:split_index])
            right=(nums[(split_index+1):])    
            return root,left,right

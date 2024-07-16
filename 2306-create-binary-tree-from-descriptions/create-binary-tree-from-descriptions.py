# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        root_dict = {}
        descriptions.sort(key=lambda x:x[0])
        child_list=set()
        nodes=set()
        highest_root = -1
        for i in descriptions:
            root,child,boolean = i
            if root not in root_dict:
                nodes.add(root)
                root_dict[root] = TreeNode(root)
            root_ = root_dict.get(root)
            if  child not in root_dict:
                nodes.add(child)
                root_dict[child] = TreeNode(child)
            child_=root_dict.get(child)
            child_list.add(child)
            if boolean:
                root_.left = child_
            else:
                root_.right = child_
        ok=(nodes-child_list).pop()
        return root_dict[ok]

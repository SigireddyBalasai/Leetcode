# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        root_dict = {}
        child_list=set()
        nodes=set()
        for i in descriptions:
            root,child,boolean = i
            if root not in root_dict:
                nodes.add(root)
                root_dict[root] = TreeNode(root)
            if  child not in root_dict:
                nodes.add(child)
                root_dict[child] = TreeNode(child)
            root_ = root_dict.get(root)    
            child_=root_dict.get(child)
            child_list.add(child)
            if boolean:
                root_.left = child_
            else:
                root_.right = child_
        ok=(nodes-child_list).pop()
        return root_dict[ok]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        arr = [root]
        list_ = [root]
        while len(arr) > 0 and len(to_delete) > 0:
            
            node = arr.pop()
            print(node.val,[i.val for i in arr])
            if node.val in to_delete:
                to_delete.remove(node.val)
                if node in list_:
                    list_.remove(node)
                if node.left != None:
                    arr.append(node.left)
                    list_.append(node.left)
                if node.right != None:
                    arr.append(node.right)
                    list_.append(node.right)
                continue   
            
            if node.left != None:
                if node.left.val in to_delete:
                    to_delete.remove(node.left.val)
                    print(f"{node.left.val} in to delete")
                    if node.left.left != None:
                        arr.append(node.left.left)
                        list_.append(node.left.left)
                    if node.left.right != None:
                        arr.append(node.left.right)
                        list_.append(node.left.right)
                    node.left = None
                else:
                    arr.append(node.left)
            if node.right != None:
                if node.right.val in to_delete:
                    to_delete.remove(node.right.val)
                    print(f"{node.right.val} in to delete")
                    if node.right.left != None:
                        arr.append(node.right.left)
                        list_.append(node.right.left)
                    if node.right.right != None:
                        arr.append(node.right.right)
                        list_.append(node.right.right)
                    node.right = None
                else:
                    arr.append(node.right)
            print(node.val,[i.val for i in arr])
        return list_
        

        
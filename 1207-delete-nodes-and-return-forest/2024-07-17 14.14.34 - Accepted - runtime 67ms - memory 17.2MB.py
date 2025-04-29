import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        def traverse(node, parentDeleted):
            deleteNode = True if node.val in to_delete else False
                
            if node.left:
                delLeft = traverse(node.left, deleteNode)
                if delLeft:
                    node.left = None
            if node.right:
                delRight = traverse(node.right, deleteNode)
                if delRight:
                    node.right = None

            if parentDeleted and not deleteNode:
                print(node.val)
                res.append(node)
            
            return deleteNode
        
        traverse(root, True)
        return res
            

            
            

        
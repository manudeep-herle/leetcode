import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.to_delete = None

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = to_delete
        self.traverse(root, True)
        return self.res

    def traverse(self, node, parentDeleted):
        deleteNode = True if node.val in self.to_delete else False
            
        if node.left:
            delLeft = self.traverse(node.left, deleteNode)
            if delLeft:
                node.left = None
        if node.right:
            delRight = self.traverse(node.right, deleteNode)
            if delRight:
                node.right = None

        if parentDeleted and not deleteNode:
            print(node.val)
            self.res.append(node)
        
        return deleteNode
        
            

            
            

        
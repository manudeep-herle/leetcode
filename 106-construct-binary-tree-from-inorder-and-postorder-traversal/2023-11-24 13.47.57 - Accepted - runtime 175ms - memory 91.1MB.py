# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree(inorder, postorder):
            if not postorder:
                print("exiting")
                return None
            
            root = TreeNode(val = postorder[-1])
            rootIndex = inorder.index(root.val)
            root.left = buildTree(inorder[0:rootIndex], postorder[0:rootIndex])
            root.right = buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
            return root
        
        return buildTree(inorder, postorder)
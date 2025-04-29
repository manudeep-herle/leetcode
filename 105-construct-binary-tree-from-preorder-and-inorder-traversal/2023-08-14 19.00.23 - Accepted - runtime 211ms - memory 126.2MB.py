# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return
        head = TreeNode(preorder[0])
        preorder = preorder[1:]
        mid = inorder.index(head.val) 
        
        # left sub tree
        head.left = self.buildTree(preorder[:mid], inorder[:mid])
        # right sub tree
        head.right = self.buildTree(preorder[mid:], inorder[mid+1:])
        
        return head
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(node):

            if val < node.val:
                # go left
                if not node.left:
                    node.left = TreeNode(val)
                    return
                insert(node.left)
            
            else:
                # go right
                if not node.right:
                    node.right = TreeNode(val)
                    return
                insert(node.right)
        
        if not root:
            root = TreeNode(val)
            
        else: 
            insert(root)

        return root

        
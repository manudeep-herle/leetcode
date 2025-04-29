# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, root, right
        ans = []
        def rec(node, ans):
            if node == None:
                return
            rec(node.left, ans)
            ans.append(node.val)
            rec(node.right, ans)
        rec(root, ans)
        return(ans)
        print(ans)

            

            
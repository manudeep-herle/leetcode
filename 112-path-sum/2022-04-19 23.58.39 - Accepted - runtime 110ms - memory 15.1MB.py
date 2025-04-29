# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def summ(node, curr_sum):
            if node == None:
                print(curr_sum)
                return False
            
            curr_sum += node.val
            
            if curr_sum == targetSum: 
                print(node.left)
                if node.left==None and node.right==None: 
                    return True
            
            return summ(node.left, curr_sum) or summ(node.right, curr_sum)
            
        return summ(root, 0)
        
        
        
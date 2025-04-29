# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(root, "\n")
        if root.left and root.right and root.left.val == root.right.val:
            def checkSymmetry(n1, n2):
                rcMatch = False
                lcMatch = False
                # Both n1 and n2 are None
                if n1 == n2 :
                    return True
                # If left child match
                if n1.left == n2.right:
                    lcMatch = True 
                elif n1.left and n2.right and n1.left.val == n2.right.val:  
                    lcMatch = checkSymmetry(n1.left, n2.right)
                    # Go one level deeper
                else: lcMatch = False

                if n1.right == n2.left:
                    rcMatch = True
                elif n1.right and n2.left and n1.right.val == n2.left.val:
                    # Go one level deeper
                    rcMatch = checkSymmetry(n1.right, n2.left)
                else: rcMatch = False
                if rcMatch and lcMatch:
                    return True
                else:
                    return False
            
            ans = checkSymmetry(root.left, root.right)
            return ans
        elif root.left == root.right:
            return True
        else: return False
            
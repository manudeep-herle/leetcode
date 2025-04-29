class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recCheck(n1, n2):
            if n1 == n2:
                return True
            if n1 and n2 and n1.val == n2.val:
                return recCheck(n1.left, n2.right) and recCheck(n1.right, n2.left)
            else:
                return False
        if not root.left and not root.right:
            return True
        return recCheck(root.left, root.right)
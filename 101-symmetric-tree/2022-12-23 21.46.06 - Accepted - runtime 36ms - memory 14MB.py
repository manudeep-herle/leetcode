class Solution:
    def isMirror(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if leftRoot == None and rightRoot == None:
            return True
        elif leftRoot != None and rightRoot != None:
            if leftRoot.val == rightRoot.val:
                    return self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)
            else:
                return False
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)
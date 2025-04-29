# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balancedRoot = TreeNode()
        self.vals = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Build a list from the unbalanced BST
        self.buildList(root)
        print(self.vals)
        self.buildTree(self.balancedRoot, 0, len(self.vals)-1)
        return self.balancedRoot

    # Inorder traversal of the BST to build sorted list
    def buildList(self, node) -> None:
        if node.left:
            self.buildList(node.left)
        self.vals.append(node.val)
        if node.right:
            self.buildList(node.right)

    def buildTree(self, node, start, end) -> None:
        if start <= end:
            mid = (start + end) // 2
            node.val = self.vals[mid]
            if mid - 1 >= start:
                node.left = TreeNode()
                self.buildTree(node.left, start, mid-1)
            if mid + 1 <= end:
                node.right = TreeNode()
                self.buildTree(node.right, mid+1, end)


        
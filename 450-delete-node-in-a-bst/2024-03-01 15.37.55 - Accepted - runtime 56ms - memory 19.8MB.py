# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val
    def predeccessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root.val = self.predeccessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


        
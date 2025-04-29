# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.ans = [[root.val]]
        self.addToLevel(root, 1)
        print(self.ans)
        return self.ans

    def addToLevel(self, head, level):
        if not head:
            return

        if len(self.ans) <= level and (head.left or head.right):
            self.ans.append([])
        
        head.left and self.ans[level].append(head.left.val)
        head.right and self.ans[level].append(head.right.val)
        
        self.addToLevel(head.left, level + 1)
        self.addToLevel(head.right, level + 1)
 
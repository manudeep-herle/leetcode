# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.ans = [[root.val]]
        self.solve(root, 1)
        print(self.ans)
        ans = []
        for li in self.ans:
            len(li) and ans.append(li[-1])
        return ans

    def solve(self, head, level):
        if not head:
            return
        if len(self.ans) <= level:
            self.ans.append([])
        if head.left:
            self.ans[level].append(head.left.val)
        if head.right:
            self.ans[level].append(head.right.val)
        
        self.solve(head.left, level + 1)
        self.solve(head.right, level + 1)
        
        

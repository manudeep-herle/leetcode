# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs
        # pass pfound and qfound to parent
        # if lca not written and pfound and qfound is true, then write lca
        # return lca
        lca = [False]
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            m = 1 if node.val == q.val or node.val == p.val else 0

            if m + r + l >= 2:
                lca[0] = node
                return 0
            return (m+r+l)

        dfs(root)

        return lca[0]

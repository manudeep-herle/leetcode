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
                return [False, False]
            [pfoundl, qfoundl] = dfs(node.left)
            [pfoundr, qfoundr] = dfs(node.right)
            pfound = (pfoundl or pfoundr or node.val == p.val)
            qfound = (qfoundl or qfoundr or node.val == q.val)

            if pfound and qfound and not lca[0]:
                lca[0] = node
            
            return ([pfound, qfound])

        dfs(root)

        return lca[0]

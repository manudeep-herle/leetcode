# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            res, res1, res2 = {"p":False, "q":False, "lca": None}, None, None
            if node.left:
                res1 = dfs(node.left)
                if res1["lca"]:
                    return res1

            if node.right:
                res2 = dfs(node.right)
                if res2["lca"]:
                    return res2

            res["p"] = (res1 and res1["p"] or res2 and res2["p"] or node.val == p.val)
            res["q"] = (res1 and res1["q"] or res2 and res2["q"] or node.val == q.val)
            if res["p"] and res["q"]:
                res["lca"] = node
            return res
        
        res = dfs(root)
        return res["lca"]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree(l, r):
            if l > r:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            rootIndex = idxMap[val]
            root.right = buildTree(rootIndex+1, r)
            root.left = buildTree(l, rootIndex - 1)
            return root
        
        idxMap = {val: idx for idx, val in enumerate(inorder)}
        return buildTree(0, len(inorder) - 1)  
        print(idxMap)
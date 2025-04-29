# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.plevel = self.qlevel = 0
        self.p, self.q = p,q
        self.pNode, self.qNode = Node(0), Node(0)
        self.goDown(root, None, 0)

        def findParent():
            while self.pNode.val != self.qNode.val and self.pNode.parent and self.qNode.parent:
                self.pNode = self.pNode.parent
                self.qNode = self.qNode.parent
            print(self.pNode.val)
            return self.pNode

        if self.plevel == self.qlevel:
            return findParent()

        elif self.plevel < self.qlevel:
            while self.plevel < self.qlevel:
                self.qNode = self.qNode.parent
                self.qlevel -= 1
            return findParent()
            
        else:
            while self.qlevel < self.plevel:
                self.pNode = self.pNode.parent
                self.plevel -= 1
            return findParent()


    def goDown(self, head, headNode, level):
        if not head:
            return

        node = Node(head.val)
        node.parent = headNode
        
        if head.val == self.p.val:
            self.pNode, self.plevel = node, level
        elif head.val == self.q.val:
            self.qNode, self.qlevel = node, level

        self.goDown(head.left, node, level + 1)
        self.goDown(head.right, node, level + 1)

        

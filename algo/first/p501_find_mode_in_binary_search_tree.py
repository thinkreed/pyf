# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.in_order_traversal(root)
        self.modes = []
        self.current_count = 0
        self.in_order_traversal(root)
        return self.modes

    def __init__(self):
        self.current_val = 0
        self.current_count = 0
        self.max_count = 0
        self.modes = None

    def count(self, val):
        if val != self.current_val:
            self.current_val = val
            self.current_count = 0

        self.current_count += 1
        if self.current_count > self.max_count:
            self.max_count = self.current_count
        elif self.current_count == self.max_count:
            if self.modes:
                self.modes.append(self.current_val)

    def in_order_traversal(self, root):
        if not root:
            return

        self.in_order_traversal(root.left)
        self.count(root.val)
        self.in_order_traversal(root.right)

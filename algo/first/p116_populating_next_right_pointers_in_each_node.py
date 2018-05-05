# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        last = root
        current = None
        while last.left:
            current = last
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            last = last.left

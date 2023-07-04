# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def isMirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (
                node1.val == node2.val and
                isMirror(node1.left, node2.right) and
                isMirror(node1.right, node2.left)
            )

        queue = [root.left, root.right]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not isMirror(node1, node2):
                return False

            if node1 is not None and node2 is not None:
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)

        return True
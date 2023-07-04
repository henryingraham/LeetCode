# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        def check_balance(node):
            if node is None:
                return True
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            if abs(left_height - right_height) > 1:
                return False
            return check_balance(node.left) and check_balance(node.right)

        return check_balance(root)
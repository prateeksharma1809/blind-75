# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/validate-binary-search-tree/
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(node, left, right):
            if node is None:
                return True
            elif node.val>left and node.val<right:
                return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root,float("-inf"), float("inf"))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inOrder(node, arr):
            if node is None:
                return arr
            else:
                arr = inOrder(node.left,arr)
                arr.append(node.val)
                arr =inOrder(node.right,arr)
                return arr
        ele = inOrder(root,[])
        return ele[k-1]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res =[root.val]
        def maxpath(node):
            if node is None:
                return 0
            leftmax = max(maxpath(node.left),0)
            rightmax = max(maxpath(node.right),0)
            res[0] =max(leftmax+rightmax+node.val,res[0])
            return node.val+max(leftmax,rightmax)
        maxpath(root)
        return res[0]
            

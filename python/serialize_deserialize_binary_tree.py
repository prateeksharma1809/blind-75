# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # def inOrder(node):
        #     if node is None:
        #         return ''
        #     res = str(inOrder(node.left))
        #     res+=str(node.val)+','
        #     res +=str(inOrder(node.right))
        #     return res
        res =[]
        def preOrder(node):
            if node is None:
                res.append('N')
                return
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        self.i =0
        def dfs():
            if arr[self.i]=='N':
                self.i+=1
                return None
            root = TreeNode(int(arr[self.i]))
            self.i+=1
            root.left = dfs()
            root.right=dfs()
            return root
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
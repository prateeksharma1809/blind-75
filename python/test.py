from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, head, root, mainHead):
        if head is None:
            return True
        if root is None:
            return False
        if root.val == head.val:
            return self.check( head.next, root.left, mainHead) or self.check(head.next, root.right, mainHead)
        return self.check( mainHead, root.left, mainHead) or self.check( mainHead, root.right, mainHead)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.check(head, root, head)


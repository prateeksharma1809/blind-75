# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        node = head
        res = None
        while node is not None:
            if node.val == 0 and node.next is not None:
                if res is None:
                    res = ListNode()
                    result = res
                else:
                    res.next = ListNode()
                    res = res.next
            else:
                res.val += node.val
            node = node.next
        return result
                
            
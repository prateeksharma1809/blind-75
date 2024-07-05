# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        res = [-1,-1]
        if head is None:
            return res
        first_crit, last_crit, index = None, None,0
        prev,curr,nxt = None, head, head.next
        while nxt is not None:
            if prev is not None and nxt is not None:
                if (curr.val<nxt.val and curr.val<prev.val) or (curr.val>nxt.val and curr.val>prev.val):
                    if first_crit is None:
                        first_crit = index
                    elif last_crit is None:
                        last_crit = index
                        res[0],res[1] = last_crit-first_crit, last_crit-first_crit
                    else:
                        diff = index-last_crit
                        if diff<res[0]:
                            res[0]=diff
                        last_crit = index
                        res[1] = last_crit - first_crit
            prev = curr
            curr = nxt
            nxt = nxt.next
            index+=1
        return res

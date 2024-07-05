package dailyChallege;

import com.leetcode.linkedlist.ListNode;

public class MinMaxCritical {

	public int[] nodesBetweenCriticalPoints(ListNode head) {
		int[] res = new int[]{-1,-1};
        if(head == null){
            return res;
        }
        int fc=-1,lc=-1,i = 0;
        ListNode prev =null, curr =head, next = curr.next;
        while(next !=null) {
        	if(prev!=null && next!=null && ((curr.val<prev.val && curr.val<next.val) || (curr.val>prev.val && curr.val>next.val))) {
        		if(fc ==-1) {
        			fc = i;
        		}else if(lc == -1) {
        			lc = i;
        			res[0]=lc-fc;
        			res[1]=lc-fc;
        		}else {
        			int diff = i - lc;
        			if(diff < res[0]) {
        				res[0]=diff;
        			}
        			res[1] = i-fc;
        			lc=i;
        		}
        	}
        	prev = curr;
        	curr = next;
        	next = next.next;
        	i++;
        }
        return res;
    }
}

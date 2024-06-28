package com.leetcode.arrays;

import java.util.ArrayList;
import java.util.List;

public class KthSmallestBst {
	
	private void inOrder(TreeNode root, List<Integer> list, int k) {
		if(list.size()>=k) {
			return ;
		}
		if(root== null) {
			return ;
		}else {
			inOrder(root.left, list,k);
			list.add(root.val);
			inOrder(root.right, list,k);
		}
	}

	public int kthSmallest(TreeNode root, int k) {
		List<Integer> list =  new ArrayList<Integer>();
		inOrder(root, list, k);
		return list.get(k-1);
	}

}

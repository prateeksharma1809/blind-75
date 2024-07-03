package com.leetcode.trees;

public class BinaryTreeMaxPath {
	
	private int max;
	private int dfs(TreeNode node) {
		if(null==node) {
			return 0;
		}
		int leftmax = Math.max(dfs(node.left), 0);
		int rightmax = Math.max(dfs(node.right), 0);
		max = Math.max(leftmax+rightmax+node.val,max);
		return node.val+Math.max(leftmax,rightmax);
	}

	public int maxPathSum(TreeNode root) {
		max = root.val;
		dfs(root);
		return max;
	}

}

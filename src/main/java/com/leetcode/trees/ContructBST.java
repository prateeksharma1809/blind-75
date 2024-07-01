package com.leetcode.trees;

import java.util.Arrays;

public class ContructBST {

	public TreeNode buildTree(int[] preorder, int[] inorder) {

		TreeNode root = new TreeNode(preorder[0]);
		int mid = -1;
		for (int i = 0; i < inorder.length; i++) {
			if (inorder[i] == preorder[0]) {
				mid = i;
				break;
			}
		}
		int[] leftPreorder = Arrays.copyOfRange(preorder, 1, mid + 1);
		int[] leftInorder = Arrays.copyOfRange(inorder, 0, mid);
		root.left = buildTree(leftPreorder, leftInorder);
		int[] rightPreorder = Arrays.copyOfRange(preorder, mid + 1, preorder.length);
		int[] rightInorder = Arrays.copyOfRange(inorder, mid + 1, inorder.length);
		root.right = buildTree(rightPreorder, rightInorder);
		return root;
	}
}

package com.leetcode.arrays;

public class MinElementInRotatedSortedArray {
	

	public int findMin(int[] nums) {
		
		int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            if (nums[l] <= nums[r]) {
                return nums[l];
            }

            int mid = (l + r) / 2;
            if (nums[mid] >= nums[l]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return 0;
	}

	public static void main(String[] args) {
		MinElementInRotatedSortedArray ms = new MinElementInRotatedSortedArray();
		System.out.println(ms.findMin(new int[] {5,1,2,3,4}));
	}

}

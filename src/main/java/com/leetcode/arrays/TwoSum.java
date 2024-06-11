package com.leetcode.arrays;

import java.util.HashMap;

public class TwoSum {
	class Solution {
	    public int[] twoSum(int[] nums, int target) {
	    	HashMap<Integer, Integer> map = new HashMap<>();
	    	for(int i=0; i<nums.length;i++) {
	    		int diff = target - nums[i];
	    		if(map.containsKey(diff)) {
	    			return new int[] {map.get(diff), i};
	    		}
	    		map.put(nums[i], i);
	    	}
	    	return null;
	    }
	}


	public static void main(String[] args) {
		TwoSum ts = new TwoSum();
		Solution s = ts.new Solution();
		for(int i : s.twoSum(new int[] {2,7,11,15}, 9)){
			System.out.print(i+" ");
		}
	}

}

package com.leetcode.arrays;

import java.util.*;

public class TopKelements {

	class Solution {
		public int[] topKFrequent(int[] nums, int k) {
			HashMap<Integer, Integer> map = new HashMap<>();
			for (int i : nums) {
				map.put(i, map.getOrDefault(i, 0) + 1);
			}
			List<List<Integer>> list = new ArrayList<>();
			for(int i =0; i <nums.length+1;i++) {
				list.add(new ArrayList<>());
			}
			for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
				List<Integer> l = list.get(entry.getValue());
				l.add(entry.getKey());
			}
			int[] result = new int[k];
			int index=0;
			for(int i=list.size()-1;i>=0;i--) {
				for(Integer j : list.get(i)) {
					result[index]=j;
					index++;
					if(index==k) {
						return result;
					}
				}
			}
			return nums;
		}
	}

	public static void main(String[] args) {
		TopKelements tp = new TopKelements();
		Solution s = tp.new Solution();
		for(int i :s.topKFrequent(new int[] {1,2,2,3,3,3}, 2)) {
			System.out.println(i);
		}

	}

}

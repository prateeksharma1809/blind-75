package dailyChallege;

import java.util.Arrays;

public class MinDist3Moves {

	public int minDifference(int[] nums) {
		int n =nums.length;
		if(nums.length<=4) 
			return 0;
		
		Arrays.sort(nums);
		int val1 = nums[n-4]-nums[0];
		int val2 = Math.min(val1, nums[n-3]-nums[1]);
		val1 = Math.min(val2, nums[n-2]-nums[2]);
		return Math.min(val1, nums[n-1]-nums[3]);
		
	}
}

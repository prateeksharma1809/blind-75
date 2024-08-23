package com.leetcode.dynamicProgramming;

public class HouseRobber {
    public int rob(int[] nums) {
        
        int[] robber_stash = new int[nums.length+1];
        robber_stash[1]=nums[0];
        for(int i=1;i<nums.length; i++){
            robber_stash[i+1]=Math.max(robber_stash[i], nums[i]+robber_stash[i-1]);

        }
        return robber_stash[nums.length];

    }
    
}

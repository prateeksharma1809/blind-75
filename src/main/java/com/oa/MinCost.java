package com.oa;

public class MinCost {
	
	public int minCost(int[] cost, int[] time) {
		int totalCost =  cost[0];
		int curr_cost = 0;
		int maxIndex = 0;
		int next_free_time = time[0]+1;
		while(next_free_time <time.length) {
			int result = checkBefore(maxIndex, next_free_time, cost, time);
			totalCost+=cost[result];
			next_free_time=result+1;
			
		}
		
		return totalCost;
	}
	
	private int checkBefore(int maxIndex, int next_free_time, int[] cost, int[] time) {
		int minIndex = next_free_time;
		int minVal = cost[next_free_time];
		for(int i=next_free_time-1; i>maxIndex;i--) {
			if(minVal>cost[i]) {
				minIndex = i;
				minVal=cost[i];
			}
		}
		return minIndex;
		
	}

	public static void main(String[] args) {
		
	}

}

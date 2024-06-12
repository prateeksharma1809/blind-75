package com.leetcode.arrays;

public class BuySellStock {
	public int maxProfit(int[] prices) {
		int l=0,r=1, maxProfit = 0;
		while(r<prices.length) {
			if(prices[r]-prices[l]>maxProfit) {
				maxProfit = prices[r]-prices[l];
			}
			if(prices[r]<prices[l]) {
				l=r;
			}
			r=r+1;
		}
		return maxProfit;
	}

	public static void main(String[] args) {
		BuySellStock bs = new BuySellStock();
		System.out.println(bs.maxProfit(new int[] {7,6,4,3,1}));
	}

}

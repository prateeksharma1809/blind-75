package com.oa;

public class NDistinctWithKVowels {

	/**
	 * Number of distinct words with K maximum contiguous vowels
	 * 
	 * You don't need to read input or print anything. Your task is to complete the
	 * function kvowelwords() which takes an Integer N, an intege K and returns the
	 * total number of words of size N with atmost K vowels. As the answer maybe to
	 * large please return answer modulo 1000000007.
	 * 
	 * @param args
	 */

	public long power(long x, long y, long p) {
		long res = 1;
		x = x % p;

		if (x == 0)
			return 0;

		while (y > 0) {
			if ((y & 1) != 0)
				res = (res * x) % p;

			y = y >> 1;
			x = (x * x) % p;
		}
		return res;

	}

	public int kvowelwords(int N, int K) {
		int i, j;
		long MOD = 1000000007;

		long[][] dp = new long[N + 1][K + 1];

		long sum = 1;
		for (i = 1; i <= N; i++) {

			dp[i][0] = sum * 21;
			dp[i][0] %= MOD;

			sum = dp[i][0];

			for (j = 1; j <= K; j++) {

				if (j > i)
					dp[i][j] = 0;

				else if (j == i) {

					dp[i][j] = power(5, i, MOD);
				} else {

					dp[i][j] = dp[i - 1][j - 1] * 5;
				}

				dp[i][j] %= MOD;
				sum += dp[i][j];
				sum %= MOD;
			}
		}
		return (int)sum;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

package com.oa;

import java.util.Arrays;

public class AirportLimousine {
    public static int collectMax(int[][] mat) {
        int n = mat.length;
        int[][][] dp = new int[n][n][n];

        for (int[][] row : dp) {
            for (int[] col : row) {
                Arrays.fill(col, Integer.MIN_VALUE);
            }
        }
        
        dp[0][0][0] = mat[0][0] == 1 ? 1 : 0;

        for (int x1 = 0; x1 < n; x1++) {
            for (int y1 = 0; y1 < n; y1++) {
                for (int x2 = 0; x2 < n; x2++) {
                    int y2 = x1 + y1 - x2;
                    if (y2 < 0 || y2 >= n || mat[x1][y1] == -1 || mat[x2][y2] == -1) {
                        continue;
                    }
                    int rider = (mat[x1][y1] == 1 ? 1 : 0) + (x1 != x2 ? (mat[x2][y2] == 1 ? 1 : 0) : 0);
                    dp[x1][y1][x2] = Math.max(dp[x1][y1][x2], getValue(dp, x1 - 1, y1, x2 - 1, mat) + rider);
                    dp[x1][y1][x2] = Math.max(dp[x1][y1][x2], getValue(dp, x1 - 1, y1, x2, mat) + rider);
                    dp[x1][y1][x2] = Math.max(dp[x1][y1][x2], getValue(dp, x1, y1 - 1, x2 - 1, mat) + rider);
                    dp[x1][y1][x2] = Math.max(dp[x1][y1][x2], getValue(dp, x1, y1 - 1, x2, mat) + rider);
                }
            }
        }

        return Math.max(0, dp[n - 1][n - 1][n - 1]);
    }

    private static int getValue(int[][][] dp, int x1, int y1, int x2, int[][] mat) {
        int y2 = x1 + y1 - x2;
        if (x1 < 0 || y1 < 0 || x2 < 0 || y2 < 0 || y2 >= mat.length || mat[x1][y1] == -1 || mat[x2][y2] == -1) {
            return Integer.MIN_VALUE;
        }
        return dp[x1][y1][x2];
    }

    public static void main(String[] args) {
        int[][] mat = {
            {0, 1, -1},
            {1, 0, -1},
            {1, 1, 1}
        };

        System.out.println(collectMax(mat)); // Output: 5
    }
}


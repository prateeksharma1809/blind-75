class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1>=m and j+1>=n:
                    continue
                elif i+1>=m and j+1<n:
                    dp[i][j] = dp[i][j+1]
                elif i+1<m and j+1>=n:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


print(Solution().uniquePaths(3,6))
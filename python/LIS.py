from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0

        # DP array where dp[i] represents the length of LIS ending at index i
        dp = [1] * length
        
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

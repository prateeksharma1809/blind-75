class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=0:
            return 0
        if n==1:
            return nums[0]
        dp = [[0 for _ in range(n+1)] for _ in range(2)]
        dp[0][1]= nums[0]
        for i in range(1,n):
            if i+1!=n:
                dp[0][i+1] = max(dp[0][i], nums[i]+dp[0][i-1])
            dp[1][i+1]= max(dp[1][i], nums[i]+dp[1][i-1])
        
        return max(dp[0][n-1], dp[1][n])
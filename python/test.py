class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp = [0 for _ in range(n+1)]
        dp[1]=1
        for i in range(1,len(nums)):
            s=i-1
            while s>0 and nums[s]>nums[i]:
                s-=1
            if nums[s]<nums[i]:
                dp[i+1]= max(dp[i], 1+dp[s+1])
            else:
                dp[i+1]=max(dp[i],1+dp[s])
        print(dp)
        return dp[n]

nums =[4,10,4,3,8,9]
Solution().lengthOfLIS(nums)
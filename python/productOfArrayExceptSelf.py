from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using pre fix and post fix sum to solve the problem
        #we store all the prefix multiplies in postion i+1
        result = [1 for _ in nums]
        for i in range(1, len(nums)):
            result[i]=nums[i-1]*result[i-1]
        # print(result)
        post=1
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*post
            post*=nums[i]
        # print(result)
        return result
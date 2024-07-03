# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=4:
            return 0
        nums.sort()
        return min(nums[-4]-nums[0],nums[-1]-nums[3],nums[-3]-nums[1],nums[-2]-nums[2])
    
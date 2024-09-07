class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tracker =  set()
        for num in nums:
            if num in tracker:
                return True
            tracker.add(num)
        return False
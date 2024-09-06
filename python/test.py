from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index_start =0
        l,r = 0, len(intervals)-1
        while l<=r:
            mid = (l+r)//2
            if intervals[mid][1]>newInterval[0]:
                r=mid-1
            else:
                l=mid+1
        print(l,r)
        res =[]
        for i in range(0, l):
            res.append(intervals[i])
        if intervals[l][0]>newInterval[0]:
            intervals[l][0]=newInterval[0]
        else:
            
        while l<len(intervals):

        
print(Solution().insert([[2,3],[4,8],[11,9]], [1,5]))
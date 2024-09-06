from typing import List
from collections import heapq

# """
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
# """

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)<=0:
            return 0
        d=1
        intervals.sort(key=lambda x:x.start)
        heap=[intervals[0].end]
        for interval in intervals[1:]:
            if len(heap)<=0 or interval.start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                d+=1
                heapq.heappush(heap,interval.end)
        return d

        
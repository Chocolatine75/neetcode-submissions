"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        intervals.sort(key= lambda pair : pair.start)
        result = 1
        rooms = [intervals[0].end]

        for  interval in intervals[1:]:

            if  rooms[0] <=interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,interval.end)
        return len(rooms)
        
        
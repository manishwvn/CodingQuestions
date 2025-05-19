class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i+1][0] < intervals[i][1]:
                return False

        return True
        
#https://leetcode.com/problems/employee-free-time/
#Time Complexity: O(nlog n)

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        free_time = []
        schedule = [i for person in schedule for i in person]
        schedule.sort(key = lambda i: (i.start, i.end))
        prev_end = schedule[0].end
        for s in schedule:
            if s.start > prev_end:
                free_time.append(Interval(prev_end,s.start))
            prev_end = max(prev_end, s.end)
        return free_time

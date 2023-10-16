"""920. Meeting Rooms(Difficulty: Easy)
https://leetcode.com/problems/meeting-rooms/
https://www.lintcode.com/problem/920/ (free version)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.((0,8),(8,10) is not conflict at 8)

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: Two times will not conflict"""


class Solution920:
    def can_attend_meetings(self, intervals: list) -> bool:
        intervals.sort()
        last = intervals[0]
        for i in intervals[1:]:
            if i[0] < last[1]:
                return False
            else:
                last = i
        return True


solution = Solution920()
print(solution.can_attend_meetings(intervals=[(0, 30), (5, 10), (15, 20)]))
print(solution.can_attend_meetings(intervals=[(5, 8), (9, 15)]))

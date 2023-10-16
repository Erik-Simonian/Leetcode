"""253 Meetgin Rooms II (Difficulty: Medium).
https://leetcode.com/problems/meeting-rooms-ii/
https://www.lintcode.com/problem/919/ (free version)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required ((0,8),(8,10) is not conflict at 8).

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation: We need two meeting rooms:
room1: (0,30)
room2: (5,10),(15,20)

Example 2:
Input: intervals = [(2,7)]
Output: 1
Explanation: Only need one meeting room"""


class Solution253:
    def min_meeting_rooms(self, intervals: list) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        result = 0
        max_rooms = 0
        start_pointer, end_pointer = 0, 0
        while start_pointer < len(intervals):
            if start[start_pointer] < end[end_pointer]:
                start_pointer += 1
                max_rooms += 1
                result = max(result, max_rooms)
            else:
                end_pointer += 1
                max_rooms -= 1

        return result


solution = Solution253()
print(solution.min_meeting_rooms(intervals=[(0, 30), (5, 10), (15, 20)]))
print(solution.min_meeting_rooms(intervals=[(2, 7)]))

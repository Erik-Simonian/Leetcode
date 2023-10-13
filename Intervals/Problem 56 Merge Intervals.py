"""56. Merge Intervals (Difficulty: Medium).
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104"""


class Solution56:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for i in intervals[1:]:
            last_max = result[-1][1]

            if i[0] <= last_max:
                result[-1][1] = max(last_max, i[1])
            else:
                result.append(i)

        return result


solution = Solution56()
print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge(intervals=[[1, 4], [4, 5]]))

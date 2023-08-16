"""84. Largest Rectangle in Histogram (Difficulty: Hard).
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg

Input: heights = [2,4]
Output: 4

Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104"""


class Solution84:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        result = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                result = max(result, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            result = max(result, h * (len(heights) - i))

        return result


solution = Solution84()
print(solution.largestRectangleArea(heights = [2,1,5,6,2,3]))
print(solution.largestRectangleArea(heights = [2,4]))

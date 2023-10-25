"""55. Jump Game (Difficulty: Medium).
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 105"""

import collections


class Solution55:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

    def canJump_2(self, nums: list[int]) -> bool:
        queue = collections.deque(nums)
        max_jump = queue[0]
        while queue:
            if max_jump >= len(queue):
                return True
            elif max_jump == 0:
                return False
            max_jump -= 1

            i = queue.popleft()
            max_jump = max(max_jump, i)

        return False


solution = Solution55()
print(solution.canJump(nums=[2, 3, 1, 1, 4]))
print(solution.canJump(nums=[3, 2, 1, 0, 4]))
print(solution.canJump_2(nums=[2, 3, 1, 1, 4]))
print(solution.canJump_2(nums=[3, 2, 1, 0, 4]))


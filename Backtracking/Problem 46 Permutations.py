"""46. Permutations (Difficulty: Medium).
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique."""


class Solution46:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(i):
            if i >= len(nums):
                result.append(nums[:])

            for x in range(i, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                backtrack(i + 1)
                nums[i], nums[x] = nums[x], nums[i]

        backtrack(0)
        return result


solution = Solution46()
print(solution.permute(nums=[1, 2, 3]))
print(solution.permute(nums=[0, 1]))
print(solution.permute(nums=[1]))

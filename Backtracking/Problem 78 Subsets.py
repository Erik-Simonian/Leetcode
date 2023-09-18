"""78. Subsets (Difficulty: Medium).
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique."""


class Solution78:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []

        # Depth-first Search
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # not include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


solution = Solution78()
print(solution.subsets(nums=[1, 2, 3]))
print(solution.subsets(nums=[0]))

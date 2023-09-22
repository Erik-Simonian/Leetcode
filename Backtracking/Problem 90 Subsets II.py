"""90. Subsets II (Difficulty: Medium).
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10"""


class Solution90:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        # Depth-first Search
        def backtracking(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtracking(i + 1, subset)
            subset.pop()

            # All subsets that DO NOT include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1, subset)

        backtracking(0, [])
        return result


solution = Solution90()
print(solution.subsetsWithDup(nums=[1, 2, 2]))
print(solution.subsetsWithDup(nums=[0]))

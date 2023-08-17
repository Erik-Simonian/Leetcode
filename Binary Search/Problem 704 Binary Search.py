"""704. Binary Search (Difficulty: Easy).
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order."""


class Solution704:
    def search(self, nums: list[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums)

        while True:
            if lower_bound == upper_bound:
                return -1

            mid_index = (lower_bound + upper_bound) // 2
            mid_item = nums[mid_index]

            if mid_item == target:
                return mid_index

            if mid_item < target:
                lower_bound = mid_index + 1
            else:
                upper_bound = mid_index


solution = Solution704()
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))

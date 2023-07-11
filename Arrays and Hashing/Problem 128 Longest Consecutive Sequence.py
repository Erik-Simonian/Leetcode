"""128. Longest Consecutive Sequence (Difficulty: Medium).

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109"""


class Solution128:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        result = 0

        for i in nums:
            if (i - 1) not in nums_set:
                length = 0
                while (i + length) in nums_set:
                    length += 1
                result = max(result, length)

        return result


solution = Solution128()
print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

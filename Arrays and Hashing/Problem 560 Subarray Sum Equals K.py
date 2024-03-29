"""560. Subarray Sum Equals K (Difficulty: Medium).
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107"""

import collections


class Solution560:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_hashmap = {0: 1}

        for n in nums:
            current_sum += n
            difference = current_sum - k

            result += prefix_hashmap.get(difference, 0)
            prefix_hashmap[current_sum] = 1 + prefix_hashmap.get(current_sum, 0)

        return result


solution = Solution560()
print(solution.subarraySum(nums=[1, 1, 1], k=2))
print(solution.subarraySum(nums=[1, 2, 3], k=3))

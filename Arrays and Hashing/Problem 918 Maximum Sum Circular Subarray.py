"""918. Maximum Sum Circular Subarray (Difficulty: Medium).
https://leetcode.com/problems/maximum-sum-circular-subarray/


Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally,
the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:
    n == nums.length
    1 <= n <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104"""


class Solution918:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]
        current_max = 0
        current_min = 0
        total = 0

        for i in nums:
            current_max = max(current_max + i, i)
            current_min = min(current_min + i, i)
            total += i
            global_max = max(global_max, current_max)
            global_min = min(global_min, current_min)

        return max(global_max, total - global_min) if global_max > 0 else global_max


solution = Solution918()
print(solution.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
print(solution.maxSubarraySumCircular(nums=[5, -3, 5]))
print(solution.maxSubarraySumCircular(nums=[-3, -2, -3]))

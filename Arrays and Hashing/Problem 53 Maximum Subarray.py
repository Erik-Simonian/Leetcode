"""53. Maximum Subarray (Difficulty: Medium).
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle."""


class Solution53:
    def maxSubArray(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = sum(nums)
        for i in range(len(nums)):
            if nums[left] <= 0 or nums[left] < nums[right]:
                left += 1
            elif nums[right] <= 0 or nums[right] <= nums[left]:
                right -= 1
            result = max(result, sum(nums[left:right]))

        return result

    def maxSubArray_2(self, nums: list[int]) -> int:
        result = nums[0]
        current_sum = 0
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            result = max(result, current_sum)

        return result


solution = Solution53()
print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(solution.maxSubArray(nums=[1]))
print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
print(solution.maxSubArray_2(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(solution.maxSubArray_2(nums=[1]))
print(solution.maxSubArray_2(nums=[5, 4, -1, 7, 8]))

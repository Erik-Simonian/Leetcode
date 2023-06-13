"""1838. Frequency of the Most Frequent Element (Difficulty: Medium).

The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation,
you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 105
    1 <= k <= 105"""


class Solution1838:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        total_sum = 0
        result = 0
        nums.sort()

        while right < len(nums):
            total_sum += nums[right]

            while nums[right] * (right - left + 1) > total_sum + k:
                total_sum -= nums[left]
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result


solution = Solution1838()
print(solution.maxFrequency(nums=[1, 2, 4], k=5))
print(solution.maxFrequency(nums=[1, 4, 8, 13], k=5))
print(solution.maxFrequency(nums=[3, 9, 6], k=2))

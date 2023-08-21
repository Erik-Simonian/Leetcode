"""347. Top K Frequent Elements (Difficulty: Medium).
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."""


class Solution347:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap_count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        result = []

        for i in nums:
            hmap_count[i] = 1 + hmap_count.get(i, 0)

        for num, count in hmap_count.items():
            frequency[count].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result


solution = Solution347()
print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(solution.topKFrequent(nums=[1], k=1))

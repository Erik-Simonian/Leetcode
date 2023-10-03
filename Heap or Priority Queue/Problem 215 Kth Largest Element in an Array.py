"""215. Kth Largest Element in an Array (Difficulty: Medium).
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104"""
import heapq


class Solution215:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        max_val = 0
        while k > 0:
            max_val = heapq.heappop(max_heap)
            k -= 1
        return abs(max_val)

    def findKthLargestWithQuickSelect(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(left, right):
            pivot = nums[right]
            pointer = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[right] = nums[right], nums[pointer]

            if pointer < k:
                return quick_select(pointer + 1, right)
            elif pointer > k:
                return quick_select(left, pointer - 1)
            else:
                return nums[pointer]

        return quick_select(0, len(nums) - 1)


solution = Solution215()
print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
print(solution.findKthLargestWithQuickSelect(nums=[3, 2, 1, 5, 6, 4], k=2))
print(solution.findKthLargestWithQuickSelect(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))


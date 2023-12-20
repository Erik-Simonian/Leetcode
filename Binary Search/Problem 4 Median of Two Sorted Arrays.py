"""4. Median of Two Sorted Arrays (Difficulty: Hard).
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106"""


class Solution4:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        array_a, array_b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(array_b) < len(array_a):
            array_a, array_b = array_b, array_a

        left, right = 0, len(array_a) - 1
        while True:
            array_a_index = (left + right) // 2
            array_b_index = half - array_a_index - 2

            a_left = array_a[array_a_index] if array_a_index >= 0 else float("-inf")
            a_right = array_a[array_a_index + 1] if array_a_index + 1 < len(array_a) else float("inf")
            b_left = array_b[array_b_index] if array_b_index >= 0 else float("-inf")
            b_right = array_b[array_b_index + 1] if array_b_index + 1 < len(array_b) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_left:
                right = array_a_index - 1
            else:
                left = array_a_index + 1


solution = Solution4()
print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))

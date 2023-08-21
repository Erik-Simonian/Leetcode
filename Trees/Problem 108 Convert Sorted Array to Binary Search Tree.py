"""108. Convert Sorted Array to Binary Search Tree (Difficulty: Easy).
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
binary search tree.

Example 1:
https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg

Example 2:
https://assets.leetcode.com/uploads/2021/02/18/btree.jpg
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution108:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def binary_search(left, right):
            if left > right:
                return None

            target = (left + right) // 2
            node = TreeNode(nums[target])
            node.left = binary_search(left, target - 1)
            node.right = binary_search(target + 1, right)
            return node

        return binary_search(0, len(nums) - 1)







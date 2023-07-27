"""513. Find Bottom Left Tree Value (Difficulty: Medium).

Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution513:
    from collections import deque
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return node.val


tree_root_1 = TreeNode(2, TreeNode(1), TreeNode(3))

tree_root_2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))

solution = Solution513()
print(solution.findBottomLeftValue(tree_root_1))
print(solution.findBottomLeftValue(tree_root_2))


"""102. Binary Tree Level Order Traversal (Difficulty: Medium).
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution102:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                result.append(level)

        return result


tree_root1 = TreeNode(3)
tree_root1.left = TreeNode(9)
tree_root1.right = TreeNode(20)
tree_root1.right.left = TreeNode(15)
tree_root1.right.right = TreeNode(7)

tree_root2 = TreeNode(1)

tree_root3 = TreeNode()

solution = Solution102()
print(solution.levelOrder(tree_root1))
print(solution.levelOrder(tree_root2))
print(solution.levelOrder(tree_root3))
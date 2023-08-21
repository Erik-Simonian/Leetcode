"""104. Maximum Depth of Binary Tree (Difficulty: Easy).
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution104:
    def maxDepth(self, root: TreeNode) -> int:      # BFS solution
        from collections import deque
        if not root:
            return 0

        queue = deque([root])
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level


solution = Solution104()
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(1, None, TreeNode(2))

print(solution.maxDepth(tree1))
print(solution.maxDepth(tree2))



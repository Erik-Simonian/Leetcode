"""124. Binary Tree Maximum Path Sum (Difficulty: Hard)

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution124:
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(node, max_sum):
            if not node:
                return 0

            left = max(dfs(node.left, max_sum), 0)
            right = max(dfs(node.right, max_sum), 0)
            max_sum = max(max_sum, left, right,  node.val + left + right)

            max_path = max(max_sum, node.val + max(left, right))
            return max(max_sum, max_path)

        return dfs(root, root.val)


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

solution = Solution124()

print(solution.maxPathSum(tree1))
print(solution.maxPathSum(tree2))
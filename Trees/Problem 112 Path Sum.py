"""112. Path Sum (Difficulty: Easy).
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution112:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def dfs(node, current_sum):
            if not node:
                return False

            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum

            return (dfs(node.left, current_sum) or
                    dfs(node.right, current_sum))

        return dfs(root, 0)


tree1 = TreeNode(5)
tree1.left = TreeNode(4)
tree1.right = TreeNode(8)
tree1.left.left = TreeNode(11)
tree1.left.left.left = TreeNode(7)
tree1.left.left.right = TreeNode(2)
tree1.right.left = TreeNode(13)
tree1.right.right = TreeNode(4)
tree1.right.right.right = TreeNode(1)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

tree3 = TreeNode()

solution = Solution112()
print(solution.hasPathSum(tree1, targetSum=22))
print(solution.hasPathSum(tree2, targetSum=5))
print(solution.hasPathSum(tree1, targetSum=0))

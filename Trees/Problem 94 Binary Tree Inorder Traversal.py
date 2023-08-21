"""94. Binary Tree Inorder Traversal (Difficulty: Easy).
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution94:
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


tree_1 = TreeNode(1,  right=TreeNode(2, TreeNode(3)))
tree_2 = TreeNode(None)
tree_3 = TreeNode(1)

solution = Solution94()
print(solution.inorderTraversal(tree_1))
print(solution.inorderTraversal(tree_2))
print(solution.inorderTraversal(tree_3))

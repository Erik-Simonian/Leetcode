"""110. Balanced Binary Tree (Difficulty: Easy).
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced

Example 1:
https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution110:
    def isBalanced(self, root: [TreeNode | None]) -> bool:

        def balanced_tree(root):
            if not root:
                return [True, 0]

            left = balanced_tree(root.left)
            right = balanced_tree(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return balanced_tree(root)[0]


tree_node4 = TreeNode(7, None, None)
tree_node3 = TreeNode(15, None, None)
tree_node2 = TreeNode(20, tree_node3, tree_node4)
tree_node1 = TreeNode(9, None, None)
tree = TreeNode(3, tree_node1, tree_node2)

tree_node2_6 = TreeNode(4, None, None)
tree_node2_5 = TreeNode(4, None, None)
tree_node2_4 = TreeNode(3, None, None)
tree_node2_3 = TreeNode(3, tree_node2_5, tree_node2_6)
tree_node2_2 = TreeNode(2, None, None)
tree_node2_1 = TreeNode(2, tree_node2_2, tree_node2_3)
tree2 = TreeNode(1, tree_node2_2, tree_node2_1)

solution = Solution110()

print(solution.isBalanced(tree))
print(solution.isBalanced(tree2))
print(solution.isBalanced(root=[]))

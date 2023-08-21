"""98. Validate Binary Search Tree (Difficulty: Medium).
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg
Input: root = [2,1,3]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution98:
    def isValidBST(self, root: TreeNode) -> bool:
        def binary_search(left, right, node):
            if not node:
                return True
            if not(right > node.val > left):
                return False

            return (binary_search(left, node.val, node.left) and
                    binary_search(node.val, right, node.right))
        return binary_search(float("-inf"), float("inf"), root)


# tree_root = TreeNode(2)
# tree_root.left = TreeNode(1)
# tree_root.right = TreeNode(3)

# tree_root_2 = TreeNode(5)
# tree_root_2.left = TreeNode(1)
# tree_root_2.right = TreeNode(4)
# tree_root_2.right.left = TreeNode(3)
# tree_root_2.right.right = TreeNode(6)

# solution = Solution98()
# print(solution.isValidBST(tree_root))
# print(solution.isValidBST(tree_root_2))






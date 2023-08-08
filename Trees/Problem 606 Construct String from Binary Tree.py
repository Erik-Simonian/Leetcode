"""606. Construct String from Binary Tree (Difficulty: Easy).
Source: https://leetcode.com/problems/construct-string-from-binary-tree/

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree
with the preorder traversal way, and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string
and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -1000 <= Node.val <= 1000"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution606:
    def tree2str(self, root: TreeNode) -> str:
        result = []

        def preorder_traversal(node):
            if not node:
                return

            result.append("(")
            result.append(str(node.val))

            if not node.left and node.right:
                result.append("()")

            preorder_traversal(node.left)
            preorder_traversal(node.right)
            result.append(")")

        preorder_traversal(root)
        result = "".join(result)
        return result[1:-1]


tree_1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
tree_2 = TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3))

solution = Solution606()
print(solution.tree2str(tree_1))
print(solution.tree2str(tree_2))
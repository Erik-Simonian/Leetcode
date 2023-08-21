"""951. Flip Equivalent Binary Trees (Difficulty: Medium).
https://leetcode.com/problems/flip-equivalent-binary-trees/

For a binary tree T, we can define a flip operation as follows: choose any node,
and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y
after some number of flip operations.
Given the roots of two binary trees root1 and root2,
return true if the two trees are flip equivalent or false otherwise.

Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Constraints:
    The number of nodes in each tree is in the range [0, 100].
    Each tree will have unique node values in the range [0, 99]."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution951:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return not root1 and not root2

        if root1.val != root2.val:
            return False

        not_flipped = self.flipEquiv(root1.left, root2.left) and \
            self.flipEquiv(root1.right, root2.right)
        flipped = self.flipEquiv(root1.left, root2.right) and \
            self.flipEquiv(root1.right, root2.left)

        return not_flipped or flipped


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)
tree1.left.right.left = TreeNode(7)
tree1.left.right.right = TreeNode(8)

tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.left.right = TreeNode(6)
tree2.right = TreeNode(2)
tree2.right.left = TreeNode(4)
tree2.right.right = TreeNode(5)
tree2.right.right.left = TreeNode(8)
tree2.right.right.right = TreeNode(7)

tree3 = TreeNode()
tree4 = TreeNode()

tree5 = TreeNode()
tree6 = TreeNode(1)

solution = Solution951()

print(solution.flipEquiv(tree1, tree2))
print(solution.flipEquiv(tree3, tree4))
print(solution.flipEquiv(tree5, tree6))

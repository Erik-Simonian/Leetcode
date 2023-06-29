"""100. Same Tree (Difficulty: Easy).

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)








tree_root1 = TreeNode(1)
tree_root1.left = TreeNode(2)
tree_root1.right = TreeNode(3)

tree_root2 = TreeNode(1)
tree_root2.left = TreeNode(2)
tree_root2.right = TreeNode(3)

tree_root3 = TreeNode(1)
tree_root3.left = TreeNode(2)

tree_root4 = TreeNode(1)
tree_root4.right = TreeNode(2)

tree_root5 = TreeNode(1)
tree_root5.left = TreeNode(2)
tree_root5.right = TreeNode(1)

tree_root6 = TreeNode(1)
tree_root6.left = TreeNode(1)
tree_root6.right = TreeNode(2)

solution = Solution100()
print(solution.isSameTree(tree_root1, tree_root2))
print(solution.isSameTree(tree_root3, tree_root4))
print(solution.isSameTree(tree_root5, tree_root6))


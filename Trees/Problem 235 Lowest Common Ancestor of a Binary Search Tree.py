"""235. Lowest Common Ancestor of a Binary Search Tree (Difficulty: Medium).

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST."""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution235:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root

        while current_node:
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node


tree_root1 = TreeNode(6)
tree_root1.left = TreeNode(2)
tree_root1.right = TreeNode(8)
tree_root1.left.left = TreeNode(0)
tree_root1.left.right = TreeNode(4)
tree_root1.left.right.left = TreeNode(3)
tree_root1.left.right.right = TreeNode(5)
tree_root1.right.left = TreeNode(7)
tree_root1.right.right = TreeNode(9)

tree_root2 = TreeNode(2)
tree_root2.left = TreeNode(1)

solution = Solution235()
print(solution.lowestCommonAncestor(tree_root1, tree_root1.left, tree_root1.right).val)
print(solution.lowestCommonAncestor(tree_root1, tree_root1.left, tree_root1.left.right).val)
print(solution.lowestCommonAncestor(tree_root2, tree_root2, tree_root2.left).val)




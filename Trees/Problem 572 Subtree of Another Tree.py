"""572. Subtree of Another Tree (Difficulty: Easy).
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints
    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution572:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.compare_trees(root, subRoot):
            return True

        return (self.compare_trees(root.left, subRoot) or
                self.compare_trees(root.right, subRoot))

    def compare_trees(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            return (self.compare_trees(tree1.left, tree2.left) and
                    self.compare_trees(tree1.right, tree2.right))

        return False


tree_root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub_root1 = TreeNode(4, TreeNode(1), TreeNode(2))

tree_root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
sub_root2 = TreeNode(4, TreeNode(1), TreeNode(2))

solution = Solution572()
print(solution.isSubtree(tree_root1, sub_root1))
print(solution.isSubtree(tree_root2, sub_root2))

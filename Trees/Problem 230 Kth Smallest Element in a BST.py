"""230. Kth Smallest Element in a BST (Difficulty: Medium).

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104
Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
and you need to find the kth smallest frequently, how would you optimize?"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution230:
    def kthSmallest(self, root: TreeNode, k: int) -> int:       # Iterative solution
        visited = 0
        stack = []
        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            visited += 1

            if visited == k:
                return current_node.val
            current_node = current_node.right


tree_root1 = TreeNode(3)
tree_root1.left = TreeNode(1)
tree_root1.right = TreeNode(4)
tree_root1.left.right = TreeNode(2)

tree_root2 = TreeNode(5)
tree_root2.left = TreeNode(3)
tree_root2.right = TreeNode(6)
tree_root2.left.left = TreeNode(2)
tree_root2.left.right = TreeNode(4)
tree_root2.left.left.left = TreeNode(1)

solution = Solution230()
print(solution.kthSmallest(tree_root1, 1))
print(solution.kthSmallest(tree_root2, 3))
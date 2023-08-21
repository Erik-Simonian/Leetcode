"""1448. Count Good Nodes in Binary Tree (Difficulty: Medium).
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.(3,4,3,5)
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4]."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1488:
    def goodNodes(self, root: TreeNode) -> int:

        def good_nodes(root, max_val):
            if not root:
                return 0

            if root.val >= max_val:
                result = 1
            else:
                result = 0

            max_val = max(max_val, root.val)
            result += good_nodes(root.left, max_val)
            result += good_nodes(root.right, max_val)
            return result

        return good_nodes(root, root.val)


tree_node1 = TreeNode(5, None, None)
tree_node2 = TreeNode(1, None, None)
tree_node3 = TreeNode(3, None, None)
tree_node4 = TreeNode(4, tree_node2, tree_node1)
tree_node5 = TreeNode(1, tree_node3, None)
tree_root1 = TreeNode(3, tree_node5, tree_node4)

tree_node2_1 = TreeNode(2, None, None)
tree_node2_2 = TreeNode(4, None, None)
tree_node2_3 = TreeNode(3, tree_node2_2, tree_node2_1)
tree_root2 = TreeNode(3, tree_node2_3, None)

tree_root3 = TreeNode(1, None, None)

solution = Solution1488()
print(solution.goodNodes(tree_root1))
print(solution.goodNodes(tree_root2))
print(solution.goodNodes(tree_root3))



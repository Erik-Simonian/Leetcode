"""199. Binary Tree Right Side View (Difficulty: Medium).
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
https://assets.leetcode.com/uploads/2021/02/14/tree.jpg
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution199:
    def rightSideView(self, root: TreeNode) -> list[int]:   # Breadth First Search method
        result = []
        queue = collections.deque([root])

        while queue:
            rightmost_element = None
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    rightmost_element = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightmost_element:
                result.append(rightmost_element.val)

        return result


tree_root1 = TreeNode(1)
tree_root1.left = TreeNode(2)
tree_root1.right = TreeNode(3)
tree_root1.left.right = TreeNode(5)
tree_root1.right.right = TreeNode(4)

tree_root2 = TreeNode(1)
tree_root2.right = TreeNode(3)

tree_root3 = TreeNode()

solution = Solution199()
print(solution.rightSideView(tree_root1))
print(solution.rightSideView(tree_root2))
print(solution.rightSideView(tree_root3))


"""114. Flatten Binary Tree to Linked List (Difficulty: Medium).
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points
    to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?"""


from binarytree import Node


class Solution114:
    def flatten(self, root: Node) -> None:
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left:
                current = root.left
                while current.right:
                    current = current.right

                current.right = root.right
                root.right = root.left
                root.left = None


tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(5)
tree1.left.left = Node(3)
tree1.left.right = Node(4)
tree1.right.right = Node(6)


solution = Solution114()
solution.flatten(tree1)
print(tree1)

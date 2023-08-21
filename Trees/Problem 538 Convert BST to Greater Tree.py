"""538. Convert BST to Greater Tree (Difficulty: Medium).
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key
of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
https://assets.leetcode.com/uploads/2019/05/02/tree.png
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -104 <= Node.val <= 104
    All the values in the tree are unique.
    root is guaranteed to be a valid binary search tree.
"""

from binarytree import Node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution538:
    def __init__(self):
        self.current_sum = 0

    def convertBST(self, root: Node) -> Node:

        if not root:
            return None

        self.convertBST(root.right)
        temp = root.val
        root.val += self.current_sum
        self.current_sum += temp
        self.convertBST(root.left)

        return root


BST_1 = Node(4, Node(1, Node(0), Node(2, right=Node(3))),
             Node(6, Node(5), Node(7, right=Node(8))))
BST_2 = Node(0, right=Node(1))

solution = Solution538()
solution2 = Solution538()

print(solution.convertBST(BST_1))
print(solution2.convertBST(BST_2))

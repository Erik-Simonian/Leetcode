"""894. All Possible Full Binary Trees (Difficulty: Medium).
https://leetcode.com/problems/all-possible-full-binary-trees/

Given an integer n, return a list of all possible full binary trees with n nodes.
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]

Constraints:
    1 <= n <= 20"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution894:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        cache = {0: [], 1: [TreeNode()]}

        def dfs(num):
            if num in cache:
                return cache[num]

            result = []
            for left in range(num):
                right = num - left - 1
                left_trees = dfs(left)
                right_trees = dfs(right)

                for tree1 in left_trees:
                    for tree2 in right_trees:
                        result.append(TreeNode(0, tree1, tree2))

            cache[num] = result
            return result

        return dfs(n)


solution = Solution894()
solution.allPossibleFBT(n=7)
solution.allPossibleFBT(n=3)

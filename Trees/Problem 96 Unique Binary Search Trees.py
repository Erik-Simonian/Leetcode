"""96. Unique Binary Search Trees (Difficulty: Medium).

Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
    1 <= n <= 19"""


class Solution96:
    def numTrees(self, n: int) -> int:
        tree_amount = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                total += tree_amount[left] * tree_amount[right]
            tree_amount[node] = total
        return tree_amount[n]


solution = Solution96()
print(solution.numTrees(n=3))
print(solution.numTrees(n=1))

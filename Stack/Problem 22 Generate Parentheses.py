"""22. Generate Parentheses (Difficulty: Medium).
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8"""


from collections import deque


class Solution22:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = deque()
        result = []

        def backtrack(n_opened, n_closed):
            if n_opened == n_closed == n:
                result.append("".join(stack))
                return

            if n_opened < n:
                stack.append("(")
                backtrack(n_opened + 1, n_closed)
                stack.pop()

            if n_closed < n_opened:
                stack.append(")")
                backtrack(n_opened, n_closed + 1)
                stack.pop()

        backtrack(0, 0)
        return result


solution = Solution22()
print(solution.generateParenthesis(n=3))
print(solution.generateParenthesis(n=1))

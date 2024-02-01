"""70. Climbing Stairs (Difficulty: Easy).
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45"""


class Solution70:
    def climbStairs(self, n: int) -> int:
        one_step, two_steps = 1, 1

        for i in range(n - 1):
            temp = one_step
            one_step = one_step + two_steps
            two_steps = temp

        return one_step


solution = Solution70()
print(solution.climbStairs(n=2))
print(solution.climbStairs(n=3))

"""994. Rotting Oranges (Difficultu: Medium).
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
https://assets.leetcode.com/uploads/2019/02/16/oranges.png
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2."""
import collections


class Solution994:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        fresh = 0
        result = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = collections.deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dir_row, dir_col in directions:
                    row += dir_row
                    col += dir_col
                    if ((row < 0 or row == len(grid)) or col < 0
                            or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            result += 1

        return result if fresh == 0 else -1


solution = Solution994()
print(solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(solution.orangesRotting(grid=[[0, 2]]))

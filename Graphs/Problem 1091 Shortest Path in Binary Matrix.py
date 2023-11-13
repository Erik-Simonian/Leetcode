"""1091. Shortest Path in Binary Matrix (Difficulty: Medium).
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected
    (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
https://assets.leetcode.com/uploads/2021/02/18/example1_1.png
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
https://assets.leetcode.com/uploads/2021/02/18/example2_1.png
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1"""
import collections


class Solution1091:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = collections.deque([(0, 0, 1)])  # row, column, length of the path
        visited = {0, 0}

        while queue:
            row, column, length = queue.popleft()
            if min(row, column) < 0 or max(row, column) >= n or grid[row][column] == 1:
                continue
            if row == n - 1 and column == n - 1:
                return length

            for dir_row, dir_col in directions:
                if (dir_row + row, dir_col + column) not in visited:
                    queue.append((dir_row + row, dir_col + column, length + 1))
                    visited.add((dir_row + row, dir_col + column))
        return - 1


solution = Solution1091()
print(solution.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))
print(solution.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(solution.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))

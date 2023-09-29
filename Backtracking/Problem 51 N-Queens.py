"""51. N-Queens (Difficulty: Hard).
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
https://assets.leetcode.com/uploads/2020/11/13/queens.jpg
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
    1 <= n <= 9"""


class Solution51:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        columns = set()
        positive_diagonals = set()
        negative_diagonals = set()
        board = [["."] * n for i in range(n)]

        def backtracking(row):
            if row == n:
                correct_board = ["".join(r) for r in board]
                result.append(correct_board)
                return

            for col in range(n):
                if col in columns or (row + col) in positive_diagonals or (row - col) in negative_diagonals:
                    continue

                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)
                board[row][col] = "Q"

                backtracking(row + 1)

                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)
                board[row][col] = "."

        backtracking(0)
        return result


solution = Solution51()
print(solution.solveNQueens(n=4))
print(solution.solveNQueens(n=1))

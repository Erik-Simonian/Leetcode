"""79. Word Search (Difficulty: Medium).
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?"""


class Solution79:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= rows or col >= columns:
                return False
            if word[index] != board[row][col] or (row, col) in visited:
                return False

            visited.add((row, col))
            result = (dfs(row + 1, col, index + 1) or
                      dfs(row - 1, col, index + 1) or
                      dfs(row, col + 1, index + 1) or
                      dfs(row, col - 1, index + 1))

            visited.remove((row, col))
            return result

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False


solution = Solution79()
print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))

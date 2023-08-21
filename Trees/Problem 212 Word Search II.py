"""212. Word Search II (Difficulty: Hard).
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
https://assets.leetcode.com/uploads/2020/11/07/search1.jpg
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
https://assets.leetcode.com/uploads/2020/11/07/search2.jpg
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique."""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True


class Solution212:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:  # Trie solution
        root = TrieNode()

        for w in words:
            root.add_word(w)

        rows = len(board)
        columns = len(board[0])
        visited = set()
        result = set()

        def dfs(row, col, node, word):
            if (row < 0 or col < 0 or
                    row == rows or col == columns or
                    (row, col) in visited or board[row][col] not in node.children):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_word:
                result.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            visited.remove((row, col))

        for r in range(rows):
            for c in range(columns):
                dfs(r, c, root, "")

        return list(result)


solution = Solution212()
print(solution.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
                                ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))
print(solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))

"""131. Palindrome Partitioning (Difficulty: Medium).
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters."""


class Solution131:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current = []

        def backtracking(i):
            if i >= len(s):
                result.append(current.copy())
                return

            for char in range(i, len(s)):
                if self.is_palindrome(s, i, char):
                    current.append(s[i:char + 1])
                    backtracking(char + 1)
                    current.pop()

        backtracking(0)
        return result

    def is_palindrome(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True


solution = Solution131()
print(solution.partition(s="aab"))
print(solution.partition(s="a"))

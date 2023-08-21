"""Problem 76. Minimum Window Substring (Difficulty: Hard).
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?"""


class Solution76:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if t == "":
            return ""
        count_t = {}
        window = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        current = 0
        target = len(count_t)
        result = [0, 0]
        result_length = float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                current += 1

            while current == target:
                if (right - left + 1) < result_length:
                    result = [left, right]
                    result_length = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    current -= 1
                left += 1

        left, right = result
        return s[left:right+1] if result_length != float('inf') else ""


solution = Solution76
print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
print(solution.minWindow(s="a", t="a"))
print(solution.minWindow(s="a", t="aa"))





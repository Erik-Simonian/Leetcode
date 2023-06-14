"""567. Permutation in String (Difficulty: Medium).

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters."""


class Solution567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        for right in range(len(s2)):
            if s2[left] in s1 and s2[right + 1] in s1:
                return True
            left += 1

        return False


solution = Solution567()
print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
print(solution.checkInclusion(s1="ab", s2="eidboaoo"))

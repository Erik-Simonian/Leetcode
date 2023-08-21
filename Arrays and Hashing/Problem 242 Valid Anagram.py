""" 242. Valid Anagram (Difficulty: Easy).
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""


class Solution242:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)

        for char in hashmap_s:
            if hashmap_s[char] != hashmap_t.get(char, 0):
                return False

        return True
        # Alternative solution using sorted()
        # return sorted(s) == sorted(t)


solution = Solution242()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))

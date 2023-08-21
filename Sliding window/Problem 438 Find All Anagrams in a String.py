"""438. Find All Anagrams in a String (Difficulty: Medium).
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters."""


class Solution438:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        count_p = {}
        count_s = {}
        left = 0

        for i in range(len(p)):
            count_p[p[i]] = 1 + count_p.get(p[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)

        if count_p == count_s:
            result = [0]
        else:
            result = []

        for right in range(len(p), len(s)):
            count_s[s[right]] = 1 + count_s.get(s[right], 0)
            count_s[s[left]] -= 1

            if count_s[s[left]] == 0:
                count_s.pop(s[left])
            left += 1

            if count_s == count_p:
                result.append(left)

        return result


solution = Solution438()
print(solution.findAnagrams(s="cbaebabacd", p="abc"))
print(solution.findAnagrams(s="abab", p="ab"))
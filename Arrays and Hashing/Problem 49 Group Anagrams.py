"""49. Group Anagrams (Difficulty: Medium).
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters."""


class Solution49:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        result = defaultdict(list)

        for i in strs:
            sorted_i = ''.join(sorted(i))
            result[sorted_i].append(i)

        return list(result.values())


solution = Solution49()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))

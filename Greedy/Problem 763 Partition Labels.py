"""763. Partition Labels (Difficulty: Medium).
https://leetcode.com/problems/partition-labels/

You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters."""


class Solution763:
    def partitionLabels(self, s: str) -> list[int]:
        result = []
        hash_map = {}  # Hashmap with the last index of every character
        partition_length = 0
        partition_end = 0

        for index, char in enumerate(s):
            hash_map[char] = index

        for i, c in enumerate(s):
            partition_length += 1
            partition_end = max(partition_end, hash_map[c])

            if i == partition_end:
                result.append(partition_length)
                partition_length = 0

        return result


solution = Solution763()
print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
print(solution.partitionLabels(s="eccbbbbdec"))

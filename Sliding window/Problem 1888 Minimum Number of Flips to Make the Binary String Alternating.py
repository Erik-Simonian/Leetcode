"""1888. Minimum Number of Flips to Make the Binary String Alternating (Difficulty: Medium).

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
    Type-1: Remove the character at the start of the string s and append it to the end of the string.
    Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.
    For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:
Input: s = "111000"
[1011]
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

Constraints:
    1 <= s.length <= 105
    s[i] is either '0' or '1'."""


class Solution1888:
    def minFlips(self, s: str):
        len_s = len(s)
        new_s = s + s        # Extended version of s to simulate Type-1 operation
        left = 0
        alt_s1 = ""          # Alternative binary version of s that starts with 0
        alt_s2 = ""          # Alternative binary version of s that starts with 1
        for i in range(len(new_s)):
            alt_s1 += "0" if i % 2 else "1"
            alt_s2 += "1" if i % 2 else "0"

        result = len(new_s)
        difference_1 = 0
        difference_2 = 0
        for right in range(len(new_s)):
            if new_s[right] != alt_s1[right]:
                difference_1 += 1
            if new_s[right] != alt_s2[right]:
                difference_2 += 1

            if (right - left + 1) > len_s:
                if new_s[left] != alt_s1[left]:
                    difference_1 -= 1
                if new_s[left] != alt_s2[left]:
                    difference_2 -= 1
                left += 1

            if (right - left + 1) == len_s:
                result = min(result, difference_1, difference_2)

        return result


solution = Solution1888()
print(solution.minFlips(s="111000"))
print(solution.minFlips(s="010"))
print(solution.minFlips(s="1110"))


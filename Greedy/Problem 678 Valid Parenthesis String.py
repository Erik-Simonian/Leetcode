"""678. Valid Parenthesis String (Difficulty: Medium).
https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'."""


class Solution678:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0

        return left_min == 0


    def checkValidString_2(self, s: str) -> bool:
        if s[0] == ")" or s[-1] == "(":
            return False

        lefts, rights, saves = 0, 0, 0

        for i in s:
            if i == "(":
                lefts += 1
            elif i == ")" and lefts > 0:
                lefts -= 1
            elif i == ")" and lefts == 0:
                rights += 1
            elif i == ")" and lefts > 0:
                lefts -= 1
            elif i == "*" and lefts > 0 or i == "*" and rights == 0:
                saves += 1

        return True if saves >= lefts + rights else False


solution = Solution678()
print(solution.checkValidString(s="()"))
print(solution.checkValidString(s="(*)"))
print(solution.checkValidString(s="(*))"))
print(solution.checkValidString(s="(*)("))
print(solution.checkValidString_2(s="()"))
print(solution.checkValidString_2(s="(*)"))
print(solution.checkValidString_2(s="(*))"))
print(solution.checkValidString_2(s="(*)("))


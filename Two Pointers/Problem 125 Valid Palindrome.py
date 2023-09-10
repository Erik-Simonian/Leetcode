"""125. Valid Palindrome (Difficulty: Easy).
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters."""


class Solution125:
    def isPalindrome(self, s: str):  # -> bool:
        # O(1) memory solution
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.check_aphanum(s[left]):
                left += 1
            while right > left and not self.check_aphanum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def check_aphanum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


solution = Solution125()
solution2 = Solution125()
print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
print(solution2.isPalindrome(s="race a car"))
print(solution.isPalindrome(s=" "))

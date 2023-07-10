"""271. Encode and Decode Strings (Difficulty: Medium).

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network
and is decoded back to the original list of strings.

Please implement encode and decode

Example

Example1

Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


class Solution271:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        for string in strs:
            result += str(len(string)) + "|" + string

        return result


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        index = 0

        while index < len(str):
            delimiter_index = index
            while str[delimiter_index] != "|":
                delimiter_index += 1
            string_length = int(str[index:delimiter_index])
            result.append(str[delimiter_index + 1: delimiter_index + 1 + string_length])
            index = delimiter_index + 1 + string_length

        return result


solution = Solution271()
print(solution.decode(solution.encode(["lint", "code", "love", "you"])))
print(solution.decode(solution.encode(["we", "say", ":", "yes"])))


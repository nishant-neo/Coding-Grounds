"""
394. Decode String
Solved
Medium

Topics

Companies
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class Solution:
    def __init__(self):
        self.result = ""
    def decodeString(self, s: str) -> str:
        def getclosebraces(s, braces_start):
            openbracescount = 0
            for i in range(braces_start+1, len(s)):
                if s[i] == '[':
                    openbracescount+=1
                if s[i] == ']':
                    openbracescount-=1
                    if openbracescount < 0:
                        return i

        def decodehelper(s, i):
            if i == len(s):
                return ""
            
            if s[i] in ['0', '1', '2', '3', '4', '5', 
                        '6', '7', '8', '9']:
                braces_start = s.find('[', i)
                braces_end = getclosebraces(s, braces_start)
                times = int(s[i:braces_start])
                str_to_be_repeated = decodehelper(s[braces_start+1: braces_end], 0)
                result = (str_to_be_repeated*times) + decodehelper(s, braces_end+1)
            else:
                result = s[i] + decodehelper(s, i+1)

            return result

        return decodehelper(s, 0)

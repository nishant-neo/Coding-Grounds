"""
1003. Check If Word Is Valid After Substitutions
Solved
Medium
Topics
Companies
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
 

Constraints:

1 <= s.length <= 2 * 104
s consists of letters 'a', 'b', and 'c'
"""

class Solution:
    def isValid(self, s: str) -> bool:

        prev = None
        while s != "" and s != prev:
            prev = s
            s = s.replace("abc", "")
        return s == ""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for elem in s:
            if (
                elem == 'c'
                and len(stack) >= 2
                and stack[-2] == 'a'
                and stack[-1] == 'b'
            ):
                stack.pop()
                stack.pop()
            else:
                stack.append(elem)
        return len(stack) == 0

        

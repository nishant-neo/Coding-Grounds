"""
3. Longest Substring Without Repeating Characters
Solved
Medium

Topics

Companies
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ch_set = set()

        l, r = 0, 0
        longest_substr = 1

        while( r < len(s)):
            if s[r] in ch_set:
                while l<r and s[r] in ch_set:
                    ch_set.remove(s[l])
                    l+=1

            ch_set.add(s[r])
            r+=1

            longest_substr = max(longest_substr, r-l)

        return longest_substr
            

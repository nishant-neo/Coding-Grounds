"""
Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

 
Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
"""

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        # Here we are genrating subset of size n-1 to 1
        # and checking if there is a repeat of that
        # Since we start with largest subset and move to smallest
        # as we get the subset we return the length of it
        for subset_size in range(n-1, -1, -1):
            hashet = set()
            for i in range(n-subset_size+1):
                
                if s[i:i+subset_size] in hashet:
                    return subset_size

                hashet.add(s[i:i+subset_size])

        return 0

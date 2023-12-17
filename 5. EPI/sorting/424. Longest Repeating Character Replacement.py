"""
424. Longest Repeating Character Replacement
Solved
Medium

Topics

Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
                
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        
        return longest_str_len
		
    # def characterReplacement(self, s: str, k: int) -> int:
    #     n = len(s)
    #     l, r = 0, 0

    #     dic = {}
    #     maxf = 0
    #     max_so_far = 0
    #     for r in range(n):
    #         dic[s[r]] = dic.get(s[r],0) + 1

            
    #         maxf = max(maxf, dic[s[r]])

    #         if (((r-l+1) - maxf) > k):
    #             dic[s[l]] = dic[s[l]]-1 
    #             l = l+1
    #         else:
    #             max_so_far = max(max_so_far, r-l+1)


    #     return max_so_far

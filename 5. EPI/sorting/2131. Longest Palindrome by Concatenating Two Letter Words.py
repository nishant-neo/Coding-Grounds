"""
2131. Longest Palindrome by Concatenating Two Letter Words
Solved
Medium

Topics

Companies

Hint
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # words_set = set(words)
        word_dic_palindrome = {}
        word_dic_reverse = {}
        
        for word in words:
            
            if word == word[::-1]:
                word_dic_reverse[word] = word_dic_reverse.get(word,0)+1
            else:
                _word = ''.join(sorted(word))
                # if word == _word:
                if _word in word_dic_palindrome:
                    word_dic_palindrome[_word].append(word)
                else:
                    word_dic_palindrome[_word] = [word]

        # print(word_dic_reverse)
        # print(word_dic_palindrome)

        count_palidrome = 0
        count_reverse = 0
        for k,v in word_dic_reverse.items():
            count_palidrome += int(v/2)
            count_reverse = v%2 if count_reverse == 0 else 1

        
        for k,v in word_dic_palindrome.items():
            count = 0
            for vv in v:
                # print()
                if vv == k:
                    count += 1
            # print(count)
            
            count_palidrome += min(count, len(v)-count)

        return 2*((count_palidrome*2)+count_reverse)


        

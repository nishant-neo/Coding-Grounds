"""
792. Number of Matching Subsequences
Solved
Medium

Topics

Companies
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        count=0
        wordMap = defaultdict(list)

        for w in words:
            wordMap[w[0]].append(w)

        for c in s:
            wordList = wordMap[c]
            wordMap[c] = []
            
            for w in wordList:
                if len(w) == 1:
                    count += 1
                else:
                    wordMap[w[1]].append(w[1:])

        return count



        # def is_sub(word):
        #     index = -1
        #     for ch in word:
        #         index = s.find(ch, index+1)
        #         if index == -1:
        #             return False
        #     return True

        # c = 0
        # for word in words:
        #     if is_sub(word):
        #         c += 1

        # return c

        
        
        
        ## TLE - got away with mem

        # mem = {}

        # matched_words = 0
        # for word in words:
        #     word_itr = 0
        #     if word in mem:
        #         matched_words += mem[word]
        #         continue
        #     mem[word] = 0
        #     for s_itr in range(len(s)):
        #         if s[s_itr] == word[word_itr]:
        #             word_itr += 1
        #         if word_itr == len(word):
        #             # print(word)
        #             mem[word] = 1
        #             matched_words += 1
        #             break
            
        # return matched_words
            

                


        

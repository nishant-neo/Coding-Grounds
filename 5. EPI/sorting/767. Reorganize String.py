"""
767. Reorganize String
Medium

Topics

Companies

Hint
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans=[]
        char_tuples = [ (-v, k) for k,v in Counter(s).items()]
        heapq.heapify(char_tuples)

        while(char_tuples):
            count_first, char_first = heappop(char_tuples)

            # check if this is the last character, if not add it 
            # and decrease the count
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0: 
                    heappush(char_tuples, (count_first + 1, char_first))
            else:
                # check if this is the last character, if it is 
                # pop a new character, if it exisits, 
                # if doesnt exists, not possible
                # other wise use that
                # and decrease the count
                if not char_tuples:
                    return ""
                count_second, char_second = heappop(char_tuples)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heappush(char_tuples, (count_second + 1, char_second))
                heappush(char_tuples, (count_first, char_first))

        return ''.join(ans)

                

        # if char_tuples[0][1] > len(s):
        #     return ""
        
        # remaining = 0
        # char_common, most_common = char_tuples[0][1]
        # if 
        # for char, count in char_tuples[1:]:



        # # for 
        
        # # most_common = char_dict.most_common(1)
        # # total = char_dict.total()

        # # remaining

        # char_dict = Counter(s)
        # most_common = char_dict.most_common(1)

        return ""
        

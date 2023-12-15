"""
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.


"""

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(s)
        modified_str = s
        sortedlist = sorted([ [idx, source, target] for idx, source, target in zip(indices, sources, targets)], reverse=True)
        # print(sortedlist)

        # Replacing from end of list wont affect the list for next coming elements
        for i ,(idx, source, target) in enumerate(sortedlist):
            len_source = len(source)
            if (idx+len_source)<=n and s[idx:idx+len_source] == source:
                modified_str = modified_str[:idx] + target + modified_str[idx+len_source:]


        return modified_str
        

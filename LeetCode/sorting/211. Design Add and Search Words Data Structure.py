"""

211. Design Add and Search Words Data Structure
Solved
Medium
Topics
Companies
Hint
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class TrieNode:
    def __init__(self, ):
        self.children = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.words = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.words
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isword = True

        

    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            
            if idx == len(word):
                return cur.isword

            if word[idx] == '.':
                for child in cur.children.values():
                    if dfs(idx+1, child):
                        return True
                return False

            elif word[idx] in cur.children:
                return dfs(idx+1, cur.children[word[idx]])
            else:
                return False

        return dfs(0, self.words)

            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

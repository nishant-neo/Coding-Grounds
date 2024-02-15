"""
737. Sentence Similarity II
Solved
Medium

Topics

Companies

Hint
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

 

Example 1:

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
Example 2:

Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: true
Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
Example 3:

Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: false
Explanation: "leetcode" is not similar to "onepiece".
 

Constraints:

1 <= sentence1.length, sentence2.length <= 1000
1 <= sentence1[i].length, sentence2[i].length <= 20
sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
0 <= similarPairs.length <= 2000
similarPairs[i].length == 2
1 <= xi.length, yi.length <= 20
xi and yi consist of English letters.

"""

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        nodes = {}
        for pairs in similarPairs:
            nodes[pairs[0]] = 1
            nodes[pairs[1]] = 1
        node_to_idx = { node:idx for idx, node in enumerate(nodes.keys())}
        idx_to_node = { idx:node for idx, node in enumerate(nodes.keys())}

        # print(idx_to_node, node_to_idx)

        parents = [i for i in range(len(idx_to_node))]
        rank = [0 for i in range(len(idx_to_node))]

        def find(node):
            p = parents[node]
            while (p != parents[p]):
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(node_a, node_b):
            p_a, p_b = find(node_a), find(node_b)

            if p_a == p_b:
                return False

            if rank[p_a] > rank[p_b]:
                parents[p_b] = p_a
                rank[p_a] += rank[p_b]

            else:
                parents[p_a] = p_b
                rank[p_b] += rank[p_a]

            return True

        for similarPair in similarPairs:
            idx1 = node_to_idx[similarPair[0]]
            idx2 = node_to_idx[similarPair[1]]
            union(idx1, idx2)

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            if (
                word1 not in node_to_idx or 
                word2 not in node_to_idx or 
                find(node_to_idx[word1]) != find(node_to_idx[word2])):
                return False


        return True


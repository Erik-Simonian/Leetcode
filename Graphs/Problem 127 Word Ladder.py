"""127. Word Ladder(Difficulty: Hard).
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence
of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique."""
import collections


class Solution127:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = collections.defaultdict(list)
        visited = {beginWord}
        result = 1
        wordList.append(beginWord)
        for word in wordList:
            for position in range(len(word)):
                pattern = word[:position] + "*" + word[position+1:]
                adj[pattern].append(word)

        queue = collections.deque([beginWord])

        while queue:
            for i in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return result
                for pos in range(len(w)):
                    pat = w[:pos] + "*" + w[pos+1:]
                    for nei_word in adj[pat]:
                        if nei_word not in visited:
                            visited.add(nei_word)
                            queue.append(nei_word)
            result += 1

        return 0


solution = Solution127()
print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))

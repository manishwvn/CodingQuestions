class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1

    def count(self, pref):
        curr = self.root
        for char in pref:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:


        trie = Trie()

        for word in words:
            if len(word) >= len(pref):
                trie.add(word)
        return trie.count(pref)
        
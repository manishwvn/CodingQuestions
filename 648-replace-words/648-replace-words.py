class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        osf = ''
        for c in word:
            if c not in node.children: break
            node = node.children[c]
            osf += c
            if node.isWord: return osf
        return word



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        
        for s in dictionary:
            trie.insert(s)
            
        result = ""
        s_list = sentence.split(" ")
        
        print(s_list)
        for word in s_list:
            if result:
                result += " "
                
            result += trie.search(word)
            
        return result
            
            
        
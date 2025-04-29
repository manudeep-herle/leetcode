class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.endOfWord = True
    
    def findRoot(self, word):
        root = ""
        node = self.root
        for c in word:
            if c in node.children:
                root += c
                node = node.children[c]
                if node.endOfWord:
                    return root
            else:
                return word
                    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build a Trie from the words in the dictionary
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        # For each word in the sentence check the trie to find the smallest match
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            root = trie.findRoot(word)
            if root:
                sentence[i] = root
        

        return " ".join(sentence)
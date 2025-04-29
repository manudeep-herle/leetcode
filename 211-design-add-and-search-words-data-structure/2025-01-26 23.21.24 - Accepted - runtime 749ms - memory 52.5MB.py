class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["endFlag"] = True

    def search(self, word: str) -> bool:
        def searchFunc(wordPointer, node):
            if wordPointer >= len(word):
                return "endFlag" in node

            if word[wordPointer] == '.':
                res = False
                for key in node.keys():
                    if key =="endFlag": continue
                    res = res or searchFunc(wordPointer + 1, (node[key]))
                return res
            else:
                if word[wordPointer] not in node:
                    return False
                return searchFunc(wordPointer+1, node[word[wordPointer]])
        
        
        return searchFunc(0, self.trie)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
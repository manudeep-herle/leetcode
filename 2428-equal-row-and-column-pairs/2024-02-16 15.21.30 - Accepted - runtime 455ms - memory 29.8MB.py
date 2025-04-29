class Trienode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = Trienode()
    
    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = Trienode()
            my_trie = my_trie.children[a] 
        my_trie.count += 1
    def search(self, list):
        head = self.trie
        for num in list:
            if num in head.children:
                head = head.children[num]
            else:
                return 0
        return head.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trie = Trie()
        count = 0
        for r in grid:
            trie.insert(r)
        
        for c in range(len(grid)):
            col = [grid[i][c] for i in range(len(grid))]
            count += trie.search(col)
        return count



        
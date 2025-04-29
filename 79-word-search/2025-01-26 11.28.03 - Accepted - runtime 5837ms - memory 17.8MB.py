class Solution:
    def __init__(self):
        self.visited = set()
        self.board = None
        self.word = None

    def outOfBounds(self, r,c):
        if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]):
            return True

    def backtrack(self, r, c, wordPointer):
        if wordPointer >= len(self.word):
            return True
        if self.outOfBounds(r,c) or self.board[r][c] != self.word[wordPointer] or (r,c) in self.visited:
            return False

        self.visited.add((r,c))
        wordPointer += 1
        res = (self.backtrack(r+1, c, wordPointer) or
        self.backtrack(r, c+1, wordPointer) or
        self.backtrack(r-1, c, wordPointer) or
        self.backtrack(r, c-1, wordPointer))

        if not res:
            self.visited.remove((r,c))

        return res


    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(m*n * word length)
        # Start at every block in the board
        # From each starting point try to build word by recursively visiting neighbors and progressing through the target
        # at each starting point the visited set is refreshed
        self.board = board
        self.word = word

        for r in range(len(board)):
            for c in range(len(board[0])):
                self.visited = set()
                if self.backtrack(r,c,0):
                    return True
        
        return False

        
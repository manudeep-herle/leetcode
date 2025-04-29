class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        print(len(s.strip().rsplit(" ")[-1]))
        return len(s.strip().rsplit(" ")[-1])
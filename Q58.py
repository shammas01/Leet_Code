class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        print(word)
        if word:
            return len(word[-1])
        else:
            return 0
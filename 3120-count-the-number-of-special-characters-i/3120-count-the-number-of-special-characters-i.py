class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for char in set(word) :
            if 'a' <= char <= 'z' and  char.upper() in word:
                count += 1
        return count
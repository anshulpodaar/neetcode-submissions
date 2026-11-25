class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        letter_count = {}
        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        for letter in t:
            letter_count[letter] = letter_count.get(letter, 0) - 1
        if any(letter_count.values()) != 0:
            return False
        else:
            return True

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(words) != len (pattern):
            return False
        characterToWord = {}
        wordToCharacter = {}
        for char, word in zip(pattern, words):
            if char in characterToWord and characterToWord[char] != word:
                return False
            if word in wordToCharacter and wordToCharacter[word] != char:
                return False
            characterToWord[char] = word
            wordToCharacter[word] = char
        
        return True
        
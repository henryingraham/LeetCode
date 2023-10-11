class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def letterCount(s:str) -> dict:
            counts = {}
            for letter in s:
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
            return counts
        count1 = letterCount(s)
        count2 = letterCount(t)
        if len(count1) != len(count2):
            return False
        for letter in count1.keys():
            if not letter in count2.keys() or count1[letter] != count2[letter]:
                return False
        return True
    
        
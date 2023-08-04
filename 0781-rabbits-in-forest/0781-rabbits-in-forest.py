class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        count = 0
        for ans in answers:
            if ans == 0:
                count += 1
            elif ans not in d.keys():
                count += ans + 1
                d[ans] = 1
            else:
                d[ans] += 1
                if d[ans] == ans + 1:
                    d.pop(ans)
        return count
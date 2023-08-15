class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0 or max(matchsticks) > total_length // 4:
            return False
        target_length = total_length // 4
        matchsticks.sort(reverse=True)

        def form_sides(i, sides):
            if i == len(matchsticks) and all(side == target_length for side in sides):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= target_length:
                    new_sides = list(sides)
                    new_sides[j] += matchsticks[i]
                    if form_sides(i+1, tuple(new_sides)):
                        return True

            return False

        return form_sides(0, (0, 0, 0, 0))
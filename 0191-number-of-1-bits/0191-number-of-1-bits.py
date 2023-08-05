class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        elif n % 2 == 0:
            return self.hammingWeight(n/2)
        return 1 + self.hammingWeight(n - 1)
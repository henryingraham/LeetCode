class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        compare = cmp_to_key(lambda x,y : int(x +y ) - int(y+x))
        update = sorted(nums, key = compare, reverse=True)
        return '0' if update[0] == '0' else ''.join(update)
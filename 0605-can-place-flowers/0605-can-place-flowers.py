class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False
        if n == 0:
            return True
        flowerbed.append(0)
        flowerbed.insert(0, 0)

        count = 0
        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 0:
                count += 1
                if count == 2:
                    if flowerbed[i+1] == 0:
                        n -= 1
                        if n == 0:
                            return True
                    count = 0
            else:
                count = 0
                    
        return False
        
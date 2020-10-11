from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        flag = 0
        for i in arr:
            if i % 2 == 1:
                if flag == 2:
                    return True
                flag += 1
            else:
                flag = 0
        return False

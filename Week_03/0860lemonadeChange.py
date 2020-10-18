from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            # 5元，不用找零
            if i == 5:
                five += 1
            # 10元，出一个5，入一个10
            elif i == 10:
                five -= 1
                ten += 1
            # 20，有10元，出一个10，出一个5
            elif ten > 0:
                ten -= 1
                five -= 1
            # 20，没有10元,出3个5
            else:
                five -= 3
            # 手中5为负数，说明手头零钱不够
            if five < 0:
                return False
        return True

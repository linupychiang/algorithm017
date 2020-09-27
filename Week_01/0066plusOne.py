from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lens = len(digits)
        for i in range(1, lens + 1):
            tmp = digits[-i] + 1
            if tmp <= 9:
                digits[-i] = tmp
                return digits
            digits[-i] = 0
            if i == lens:
                digits.insert(0, 1)
                return digits

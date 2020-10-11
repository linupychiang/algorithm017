from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums = [i * i for i in A]
        nums.sort()
        return nums

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lens = len(height)
        max_nums = 0
        i, j = 0, lens - 1
        while i < j:
            if height[i] < height[j]:
                max_nums = max(max_nums, height[i] * (j - i))
                i += 1
            else:
                max_nums = max(max_nums, height[j] * (j - i))
                j -= 1
        return max_nums

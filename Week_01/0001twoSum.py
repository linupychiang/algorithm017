from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return [tmp[target - nums[i]], i]
            else:
                tmp[nums[i]] = i

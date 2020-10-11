from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans


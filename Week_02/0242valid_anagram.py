import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmp = collections.defaultdict(int)
        for i in s:
            tmp[i] += 1
        for i in t:
            tmp[i] -= 1
            if tmp[i] < 0:
                return False
        return True

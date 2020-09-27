class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        s1, s2 = 1, 2
        for i in range(3, n + 1):
            s3 = s1 + s2
            s1 = s2
            s2 = s3
        return s3

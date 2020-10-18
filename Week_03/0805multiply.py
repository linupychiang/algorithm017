class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 1:
            return B
        if B == 1:
            return A
        if A <= B:
            return B + self.multiply(A - 1, B)
        else:
            return A + self.multiply(A, B - 1)

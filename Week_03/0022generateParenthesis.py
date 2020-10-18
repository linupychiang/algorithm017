from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.gen(0, 0, n, result, "")
        return result

    def gen(self, left, right, n, result, res):
        if right == n:
            result.append(res)
            return res
        if left < n:
            self.gen(left + 1, right, n, result, res + "(")
        if right < left:
            self.gen(left, right + 1, n, result, res + ")")

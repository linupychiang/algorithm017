from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if len(result) < len(A[0]):
                    result.append([A[i][j]])
                else:
                    result[j].append(A[i][j])
        return result

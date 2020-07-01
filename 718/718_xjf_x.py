# 法一: DP O(N*N)
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for j in range(len(B) + 1)] for i in range(2)]
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                dp[(i + 1) % 2][j + 1] = dp[i % 2][j] + 1 if A[i] == B[j] else 0
                res = max(res, dp[(i + 1) % 2][j + 1])
        return res
# 没想出来，关键在于拆分目标
# A[i] + A[j] - (j-i) 拆分成 A[i]+i + A[j]-j 遍历每一个j，但是A[i]+i的最大值可以通过一次遍历完成
# 其中 i<j


class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        aii = A[0]+0
        res = -1
        for i in range(1, len(A)):
            res = max(res, A[i]-i+aii)
            aii = max(aii, A[i]+i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))

from typing import List

# O(n^2) 的 dp
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         lp = len(prices)
#         if lp == 0: return 0
#         dp = [-1] * lp
#         dp[-1] = 0
#         for i in range(lp - 2, -1, -1):
#             dp[i] = dp[i + 1]
#             for j in range(i + 1, lp):
#                 diff = prices[j] - prices[i]
#                 if diff < 0: continue
#                 if diff == 0: dp[i] = max(dp[i], dp[j])
#                 else: dp[i] = max(dp[i], diff + (dp[j + 2] if j + 2 < lp else 0))
#         return dp[0]

# 题解的 O(n) 的 dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = len(prices)
        if lp == 0: return 0
        dp = [[0 for j in range(3)] for i in prices] # 已买、冷冻期、不在冷冻期
        dp[0][0] = -prices[0]
        for i in range(1, lp):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1][1], dp[-1][2])


print(Solution().maxProfit([1,2,3,0,2]))
print(Solution().maxProfit([1,2,4,0,4]))
print(Solution().maxProfit([1,2,4,0,3]))
print(Solution().maxProfit([1,2,4,0,2]))
print(Solution().maxProfit([1,2,4,0,1]))
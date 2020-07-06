# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         row = len(obstacleGrid)
#         col = len(obstacleGrid[0])
#         cnt = [[0 for j in range(col)] for i in range(row)]
#         cnt[row - 1][col - 1] = 1
#         def dfs(x, y):
#             if x >= row or y >= col or obstacleGrid[x][y] == 1: return 0
#             if cnt[x][y] > 0: return cnt[x][y]
#             cnt[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
#             return cnt[x][y]
#         return dfs(0, 0)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [0 for j in range(col)]
        dp[0] = 1
        for i in range(row):
            if obstacleGrid[i][0] == 1: dp[0] = 0
            for j in range(1, col):
                if obstacleGrid[i][j] == 1: dp[j] = 0
                else: dp[j] += dp[j - 1]
        return dp[-1]
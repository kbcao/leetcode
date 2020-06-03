# dp做，dp[i] 表示目前得分为i的情况下能够获胜的概率，从后往前推
# 在和为 K-1 时候抽可能会到达最大值 K-1+W
# 当 N > K-1+W , 在 [K, K-1+W] 内获胜概率为 1, (K-1+W, N] 获胜概率为0（因为不可到达）
# 当 N < K-1+W , 在 [K, N] 内获胜概率为 1
# 从 K-1 往前，每一个dp值都等于后W个的平均：在当前情况下抽 1, 2, 3 ... ,W 的情况下获胜概率的平均
# 其实可以看到，当 N > K-1+W 的时候，K-1 以及往前的获胜概率其实都是1，因为当前值之后的W个全是1，所以可以优化下

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W - 1:
            return 1
        dp = [0.] * (K + W)
        for i in range(K, N + 1):
            dp[i] = 1
        for i in range(K - 1, -1, -1):
            # 计算当前情况下抽到1, 2, 3 ... ,W 的情况下获胜概率的平均
            for j in range(1, W + 1):
                dp[i] += dp[i + j]
            dp[i] /= W
        return dp[0]


# 复杂度太高会TLE，因此需要把计算dp[0..K-1]的式子优化为相临两项的递推式


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W - 1:
            return 1
        dp = [0.] * (K + W)
        for i in range(K, N + 1):
            dp[i] = 1
        # 第K-1的时候的获胜概率需要单独计算，因为不能用递推式子
        dp[K - 1] = float(N - K + 1) / W
        for i in range(K - 2, -1, -1):
            # 使用递推式dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    print(s.new21Game(29, 17, 10))

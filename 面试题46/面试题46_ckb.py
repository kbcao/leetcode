# dp
# 假如在末尾添加一位，则有两种可能：
# 1. 如果不能和前面一位能组成10-25之间的数字，那么就 =dp[i-1]
# 2. 如果能的话，就 =dp[i-1](拆开来组)+dp[i-2]（合并成一个）


class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        nums = str(num)
        dp = [0]*len(nums)
        dp[0] = 1
        dp[1] = 2 if 10 <= int(nums[:2]) <= 25 else 1
        for i in range(2, len(nums)):
            dp[i] = dp[i-1]+(dp[i-2] if 10 <= int(nums[i-1:i+1]) <= 25 else 0)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.translateNum(12258))

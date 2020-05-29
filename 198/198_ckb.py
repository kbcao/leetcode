# 没想到用dp
# 状态转移方程：=之前的一家不偷，这家偷（dp(i-2) + val(i)）和上一家偷了（dp(i-1)）的较大值

class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        dp=[0]*len(nums)
        dp[0]=nums[0]
        if len(nums)>=2:
            dp[1]=max(nums[0:2])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,1,3]))


        
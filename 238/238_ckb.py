# 用一个变量记录着当前值左边的连乘结果，然后当前结果*=这个值
# 从左端点和从右端点分别走一趟就结束了
# easy

class Solution:
    def productExceptSelf(self, nums):
        res=[1]*len(nums)
        aproduct=1
        for i in range(1,len(nums)):
            aproduct*=nums[i-1]
            res[i]*=aproduct
        aproduct=1
        for i in range(len(nums)-2,-1,-1):
            aproduct*=nums[i+1]
            res[i]*=aproduct
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))

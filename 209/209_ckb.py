# 想到的是nlogn的解法，前缀和，然后因为全是正数，前缀和是递增的，因此对于前缀和的每一个元素，二分查找右边的目标值
# 其实可以用n的解法：双指针，小的时候j右移，大的时候i右移，同时维护最小长度（结果）


from typing import List
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        res = n+1
        for i in range(n):
            target = s+prefix_sum[i]
            j = bisect.bisect_left(prefix_sum, target)
            if j <= n:
                res = min(res, j-i)
        return 0 if res == n+1 else res


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))

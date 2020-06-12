# 把三数和转换为 有序数组的两数和 问题（双指针头尾指可解）
# 因此先排序，然后遍历每一个<0的数字，看其右边存不存在 两数和=target-它 的情况


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n <= 2:
            return []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n-1
            target = -nums[i]
            while L < R:
                if nums[L]+nums[R] == target:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[L]+nums[R] > target:
                    R -= 1
                else:
                    L += 1
        return res

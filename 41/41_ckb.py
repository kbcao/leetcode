# 最重要的是：结果只可能在 1 到 len(n)+1 之间
# 因此只需要把当前元素放到idx为其值的地方，最后遍历一遍，第一个idx不为值的就是结果了
# “放”的过程使用交换实现，但是对于交换过来的值，也要把他放到正确的位置，直到该值 <1 或者 >n

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                target = nums[i] - 1
                nums[target], nums[i] = nums[i], nums[target]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))

# 1. 二分查找，直接查找具体的idx数组（原数组只用来统计比该idx小的元素个数，从而知道该往左还是往右走）
# 2. 针对每一二进制位，统计1-n的为1的个数之和，以及nums中1的个数之和，后者某一位比前者多，则这一位为1，最后得到结果
# 3. 因为有两个idx都是同一个数字，并且value都可以被作为idx，所以idx->value的图中存在环，用快慢指针找到环的入口即为答案


class Solution:
    def findDuplicate(self, nums):
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            lower_cnt = 0
            for num in nums:
                # 统计的时候一定要把=的情况统计进去
                lower_cnt += 1 if num <= mid else 0
            if lower_cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:
    def findDuplicate(self, nums):
        _len = len(nums)
        one2n_binary_cnt = [0] * (len(bin(_len - 1)[2:]))
        for i in range(1, _len):
            i_binary = bin(i)[2:]
            for j in range(len(i_binary) - 1, -1, -1):
                one2n_binary_cnt[j - len(i_binary)] += 1 if i_binary[j] == '1' else 0
        nums_binary_cnt = [0] * len(one2n_binary_cnt)
        for num in nums:
            i_binary = bin(num)[2:]
            for j in range(len(i_binary) - 1, -1, -1):
                nums_binary_cnt[j - len(i_binary)] += 1 if i_binary[j] == '1' else 0
        res = ['1' if nums_binary_cnt[i] > one2n_binary_cnt[i] else '0' for i in range(len(nums_binary_cnt))]
        return int(''.join(res), 2)


class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while (slow == 0 and fast == 0) or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([2, 2, 2, 2, 2]))

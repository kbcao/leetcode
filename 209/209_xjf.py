class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, sum_n, min_len = 0, 0, len(nums) + 100
        for right in range(0, len(nums)):
            sum_n += nums[right]
            while sum_n - nums[left] >= s:
                sum_n -= nums[left]
                left += 1
            if sum_n >= s:
                min_len = min(min_len, right - left + 1)
        return min_len if min_len < len(nums) + 100 else 0
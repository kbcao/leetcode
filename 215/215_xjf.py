# 用堆 100ms
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.build(nums, i, size)
        for i in range(k - 1):
            size -= 1
            nums[0], nums[size] = nums[size], nums[0]
            self.build(nums, 0, size)
        return nums[0]
    
    def build(self, nums: List[int], root: int, size: int):
        left, right, big = root * 2 + 1, root * 2 + 2, root
        if left < size and nums[left] > nums[big]:
            big = left
        if right < size and nums[right] > nums[big]:
            big = right
        if big != root:
            nums[root], nums[big] = nums[big], nums[root]
            self.build(nums, big, size)

# 用快排 44ms
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick(nums, k, 0, len(nums))

    def quick(self, nums, k, left, right):
        t = left + (right - left) // 2
        x = nums[t]
        l, r = left, right - 1
        nums[t], nums[r] = nums[r], nums[t]
        while l < r:
            while l < r and nums[l] > x: l += 1
            if l < r: nums[l], nums[r] = nums[r], nums[l]
            while l < r and nums[r] <= x: r -= 1
            if l < r: nums[l], nums[r] = nums[r], nums[l]
        if l + 1 == k: return nums[l]
        if l + 1 < k: return self.quick(nums, k, l + 1, right)
        return self.quick(nums, k, left, l)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [0, 0]
        i = 0
        for n in nums:
            i = (i + 1) % 2
            arr[i] = max(arr[i - 1], arr[i] + n)
        return arr[i]
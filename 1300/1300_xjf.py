class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        ln = len(arr)
        arr.sort()
        arr.insert(0, 0)
        arr_sum = arr.copy()
        for i in range(1, ln + 1): arr_sum[i] += arr_sum[i - 1]
        # 二不二分其实无所谓, 时间复杂度的大头是排序 O(nlogn), 下面用遍历也就 O(n)
        # for i in range(ln): # 本来应该是 ln - 1, 但是 insert 了一个 0, 于是刚好是 ln
        #     v = (target - arr_sum[i]) // (ln - i)
        #     if v < arr[i + 1]:
        #         d1 = abs(target - arr_sum[i] - v * (ln - i))
        #         d2 = abs(target - arr_sum[i] - (v + 1) * (ln - i))
        #         return min(arr[ln], v + (1 if d1 > d2 else 0))
        # return arr[ln]

        # 但是还是写了个二分版本 (——,——), 结果提交上去时间果然完全没区别 (都是64ms)
        l, r = 0, ln
        while True:
            m = l + r >> 1
            v = (target - arr_sum[m]) // (ln - m)
            if v < arr[m]: r = m
            elif v >= arr[m + 1] and m < ln -1: l = m
            else:
                d1 = abs(target - arr_sum[m] - v * (ln - m))
                d2 = abs(target - arr_sum[m] - (v + 1) * (ln - m))
                return min(arr[ln], v + (1 if d1 > d2 else 0))
        return arr[ln]
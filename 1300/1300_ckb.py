# 不难
# 先排序，然后找到 最后一个满足的 和 第一个不满足 的，对于 这两个值 中间的 那些值 用二分去找


class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        n = len(arr)
        i = 0
        asum = 0
        while i < n and (asum+(n-i)*arr[i]) <= target:
            asum += arr[i]
            i += 1
        if i == n:
            return arr[-1]

        def binarySearch(l, r):
            if l > r:
                return r
            mid = (l+r)//2
            t = asum+(n-i)*mid
            if t == target:
                return mid
            elif t > target:
                return binarySearch(l, mid-1)
            else:
                return binarySearch(mid+1, r)

        left = binarySearch((arr[i-1] if i >= 1 else 0), arr[i])
        right = left+1
        return left if abs(asum+(n-i)*left-target) <= abs(asum+(n-i)*right-target) else right


if __name__ == "__main__":
    s = Solution()
    print(s.findBestValue([4, 9, 3], 10))

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        arr = [0x7fffffff] * len(triangle)
        arr[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            arr[i] = arr[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                arr[j] = min(arr[j - 1], arr[j]) + triangle[i][j]
            arr[0] = arr[0] + triangle[i][0]
        return min(arr)
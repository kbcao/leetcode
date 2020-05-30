# 没做出来
# 第一个要想要的是，要选取一根柱子作为“基准高度”（木板的最下沿）然后看左边和右边分别能够维持多长（越长越好）
# 也就是要分别找到 左边和右边 比当前柱子小的第一个柱子，可以通过 单调栈 一次性全部找好备用

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_first_samller = [-1]*n
        right_first_smaller = [-1]*n
        # 找左边的第一个比当前值小的
        mono_stack = []
        for i in range(len(heights)):
            while len(mono_stack) > 0 and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left_first_samller[i] = mono_stack[-1] if len(
                mono_stack) > 0 else -1
            mono_stack.append(i)
        # 找右边的第一个比当前值小的
        mono_stack = []
        for i in range(len(heights)-1, -1, -1):
            while len(mono_stack) > 0 and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right_first_smaller[i] = mono_stack[-1] if len(
                mono_stack) > 0 else n
            mono_stack.append(i)
        res = max(heights[i]*(right_first_smaller[i]-left_first_samller[i]-1)
                  for i in range(n)) if n > 0 else 0
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))

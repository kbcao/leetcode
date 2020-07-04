# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         vis = [-1] * len(s)
#         left, right = -1, -2
#         for i in range(len(s) - 1):
#             l, r = i, i + 1
#             while True:
#                 while l >= 0 and r < len(s) and s[l] =='(' and s[r] == ')':
#                     vis[l], vis[r] = r, l
#                     l -= 1
#                     r += 1
#                 if l >= 0 and vis[l] != -1: l = vis[l] - 1
#                 else: break
#             if r - l - 1 > right - left: left, right = l + 1, r - 1
#         return right - left + 1

# 更好的空间 O(1) 的方法: 从左/右各遍历一遍, 记录左右括号个数, 当右括号/左括号超出的时候置零
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        for i in range(2):
            st, cnt = 0, 0
            for c in s[::-2 * i + 1]:
                st += (1 if c == '()'[i] else -1)
                if st < 0: st = cnt = 0
                else:
                    cnt += 1
                    if st == 0: res = max(res, cnt)
        return res
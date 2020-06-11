# 单调栈的应用
# easy

class Solution:
    def dailyTemperatures(self, T):
        mono_stack=[]
        res=[0]*len(T)
        for i in range(len(T)):
            while mono_stack and T[i]>mono_stack[-1][0]:
                res[mono_stack[-1][1]]=i-mono_stack[-1][1]
                mono_stack.pop()
            mono_stack.append((T[i],i))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


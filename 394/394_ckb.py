# 遇到 ] 就出栈，计算完把结果继续进栈 easy

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                num = int(s[idx])
                while idx + 1 < len(s) and s[idx + 1].isdigit():
                    num = num * 10 + int(s[idx + 1])
                    idx += 1
                stack.append(num)
            elif s[idx].isalpha():
                string = s[idx]
                while idx + 1 < len(s) and s[idx + 1].isalpha():
                    string += s[idx + 1]
                    idx += 1
                stack.append(string)
            elif s[idx] == ']':
                string=[]
                while stack[-1] !='[':
                    string.append( stack.pop())
                assert stack.pop() == '['
                cnt = stack.pop()
                stack.append(''.join(string[::-1]) * cnt)
            else:
                stack.append(s[idx])
            idx += 1
        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString('3[a2[c]]'))

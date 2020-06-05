# 这个和填数字很像，但是填数字是方形的，这个是普通矩形，所以可能出现最后重复的情况
# 在大while下的每个for后面都判断下是否结束即可
# 还算easy

class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==0: return []
        res = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while l <= r and t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b or l > r: break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if t > b or l > r: break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b or l > r: break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

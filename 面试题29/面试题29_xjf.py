class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return matrix;
        w, h = len(matrix[0]), len(matrix)
        res = []
        for i in range((min(w, h) + 1) // 2):
            for j in range(i, w - i): res.append(matrix[i][j])
            for j in range(i + 1, h - i): res.append(matrix[j][w - i - 1])
            if h - 2 * i > 1:
                for j in range(w - i - 2, i - 1, -1): res.append(matrix[h - i - 1][j])
            if w - 2 * i > 1:
                for j in range(h - i - 2, i, -1): res.append(matrix[j][i])
        return res
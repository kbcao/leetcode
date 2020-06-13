# fibnacci

class Solution:


    def fib_formula(self,n):
        import math
        denominator = math.sqrt(5)
        return int((pow((1+denominator)/2, n) - pow((1-denominator)/2, n)) / denominator)

    def mul(self,a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += a[i][k] * b[k][j]
        return c

    def fib_matrix(self,n):
        if n <= 1:
            return max(n, 0)
        res = [[1, 0], [0, 1]]  # 单位矩阵
        A = [[1, 1], [1, 0]]  # A矩阵
        while n:
            if n & 1:
                res = self.mul(res, A)  # 如果n是奇数，或者直到n=1停止条件
            A = self.mul(A, A)  # 快速幂
            n >>= 1  # 整除2，向下取整
        return res[0][1]
    

    def climbStairs(self, n: int) -> int:
        return self.fib_matrix(n+1)

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(38))

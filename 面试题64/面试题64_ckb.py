# 没做出来
# 其实递归很容易想，就是递归中止条件不用if就只能用短路运算符，python中 
# 0 and 任何 =0
# 非0 and 任何 = 任何

# 还有用快速乘法做的
# A 乘 B就是 B最后一位是1的时候，res+=A, 然后B右移一位，A左移一位，一直循环
# 这道题用这个乘法来实现n*(n+1)

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n+self.sumNums(n-1)


class Solution:
    def sumNums(self, n: int) -> int:
        n_np1=0
        A=n
        B=n+1
        # 这个while会执行最多14次， 因为 n+1 最大也就 10 0111 0001 0001‬，要不使用while就复制14遍即可（多执行没事）
        while B:
            n_np1+= (B&1 and A)
            A<<=1
            B>>=1
        return n_np1>>1



if __name__ == "__main__":
    s = Solution()
    print(s.sumNums(10))

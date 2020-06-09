# 只翻转后一半的数字（靠反转后的大于前一半），翻转完相等或者比前面部分多出一位，12 和123是可以的，
# 10是个特例，翻转完后变成 0 和 1，1/10==0，但是10不是回文，所以要第一部处理，0结束的都不是回文

class Solution:
    def isPalindrome(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False
        res=0
        while res<x:
            res=res*10+(x%10)
            x//=10
        return x==res or x==res//10

       

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10))

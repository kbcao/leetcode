# 比较直接，首先想到的是 从后往前递归 做
# 但其实每次计算 * 的可能性的时候，重复计算了前面的某些结果
# 可以用一个全局二维数组保存下 某个子串s 和 某个子匹配p 是否匹配


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)==0 and len(p)==0:return True
        if len(s)!=0 and len(p)==0:return False
        if len(s)==0 and len(p)!=0:
            return len(p)>=2 and p[-1]=='*' and self.isMatch(s,p[:-2])
        last_p=p[-1]
        if last_p.isalpha():
            if last_p!=s[-1]:return False
            return self.isMatch(s[:-1],p[:-1])
        elif last_p=='.':
            return self.isMatch(s[:-1],p[:-1])
        elif last_p=='*':
            if len(p)==1:return False
            second_p=p[-2]
            if second_p==s[-1] or second_p=='.':
                #      *代表1，用完                     *代表1以上，用完继续用       *代表0
                return self.isMatch(s[:-1],p[:-2]) or self.isMatch(s[:-1],p) or self.isMatch(s,p[:-2])
            else:
                #      *只能用0次
                return self.isMatch(s,p[:-2])

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("a","ab*"))

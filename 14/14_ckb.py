# 每次比较所有字符串的第i个字符
# 还有横向的方法：先把str1当成res，然后分别看后面的str，计算他们和res之间的最短前缀
# 还可以用字典树，结点有且仅有一个孩子，且碰到一个叶结点就结束
# python 中还可以用zip(*strs)转换成('a','a','a'),('a','a','a'),('a','a','a')分别代表第一位、第二位、第三位在各个字符串上的值

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        lcp=''
        idx=0
        while True:
            if idx>=len(strs[0]):
                break
            c=strs[0][idx]
            for str in strs[1:]:
                if idx>=len(str) or str[idx]!=c:
                    return lcp
            lcp+=c
            idx+=1
        return lcp
        


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))

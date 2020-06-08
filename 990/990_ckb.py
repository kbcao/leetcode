# 并查集的使用，easy，但要注意并查集如果要优化要用到rank
# rank初始化为0，然后union的时候把rank小的放到rank大的上面

class Solution:
    def equationsPossible(self, equations) -> bool:
        search=[i for i in range(26)]
        def find(x):
            if x!=search[x]:
                search[x]=find(search[x])
            return search[x]
        def union(x,y):
            x=find(x)
            y=find(y)
            if x==y:return
            search[x]=y
        for e in equations:
            if e[1]=='=':
                union(ord(e[0])-ord('a'),ord(e[3])-ord('a'))
        for e in equations:
            if e[1]=='!':
                if find(ord(e[0])-ord('a'))==find(ord(e[3])-ord('a')):
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.equationsPossible(["a==b","b!=a"]))


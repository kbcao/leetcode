# 思路和题解一样，但是在建图时就超时，应该是 Python 太慢。 O(N*N*K+N) = O(N*N*K)
import queue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 建图
        try:
            i = wordList.index(beginWord)
            wordList[0], wordList[i] = wordList[i], wordList[0]
        except ValueError: wordList.insert(0, beginWord)
        try:
            i = wordList.index(endWord)
            wordList[-1], wordList[i] = wordList[i], wordList[-1]
        except ValueError: return []
        l = len(wordList)
        mat = [[] for i in range(l)]
        for i in range(l):
            for j in range(i + 1, l):
                d = 0
                for k in range(len(wordList[0])):
                    if wordList[i][k] != wordList[j][k]: d += 1
                if d == 1:
                    mat[i].append(j)
                    mat[j].append(i)

        # BFS
        path = [-1 for i in range(l)]
        q = queue.Queue()
        q.put((0, 0))
        while not q.empty():
            p, x = q.get()
            if path[p] != -1: continue
            path[p] = x
            for i in mat[p]:
                if path[i] == -1: q.put((i, x + 1))
        
        q.put((l - 1, [endWord]))
        res = []
        while not q.empty():
            p, arr = q.get()
            if p == 0:
                arr.reverse()
                res.append(arr)
                continue
            for i in mat[p]:
                new_arr = arr.copy()
                new_arr.append(wordList[i])
                if path[i] == path[p] - 1: q.put((i, new_arr))
        return 

# 建图改成字典树，过了。 O(N*K*26+N) = O(N*K)
import queue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 把 wordList 改造成 Word-ID 表
        try: # 把 beginWord 挪到最前面
            i = wordList.index(beginWord)
            wordList[0], wordList[i] = wordList[i], wordList[0]
        except ValueError: wordList.insert(0, beginWord)
        try: # 把 endWord 挪到最后面
            i = wordList.index(endWord)
            wordList[-1], wordList[i] = wordList[i], wordList[-1]
        except ValueError: return []
        l, wl = len(wordList), len(wordList[0])

        # 建字典树
        dic = {}
        for i in range(l):
            d = dic
            for c in wordList[i]:
                if c not in d: d[c] = {}
                d = d[c]
            d['id'] = i

        # 建图
        mat = [[] for i in range(l)]
        for i in range(l):
            w = wordList[i]
            d = dic
            for j in range(wl):
                for c in d:
                    if c == w[j]: continue
                    d2 = d[c]
                    for k in range(j + 1, wl):
                        if w[k] in d2: d2 = d2[w[k]]
                        else: break
                    if 'id' in d2:
                        mat[i].append(d2['id'])
                if w[j] not in d: break
                d = d[w[j]]

        # BFS
        path = [-1 for i in range(l)]
        q = queue.Queue()
        q.put((0, 0))
        while not q.empty():
            p, x = q.get()
            if path[p] != -1: continue
            path[p] = x
            for i in mat[p]:
                if path[i] == -1: q.put((i, x + 1))
        
        # 遍历所有最短路径
        q.put((l - 1, [endWord])) # BFS的时候是正着的，现在倒着遍历会快一点
        res = []
        while not q.empty():
            p, arr = q.get()
            if p == 0:
                arr.reverse()
                res.append(arr)
                continue
            for i in mat[p]:
                new_arr = arr.copy()
                new_arr.append(wordList[i])
                if path[i] == path[p] - 1: q.put((i, new_arr))
        return res
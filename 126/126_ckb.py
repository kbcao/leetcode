from collections import defaultdict, deque
import string

# 解法一：
# 先bfs按照层次找到当前结点的所有下一层可达到的结点，保存起来（碰到结果了立刻中止，即：只返回最短的层数的结果）
# 然后dfs遍历搜索
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        # 先通过bfs找到 节点的所有可到达的后继结点（下一层），记录到successors中（通过层次遍历，不重复）
        successors = defaultdict(set)
        found = self._bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 然后进行dfs搜索看能不能到达endWord
        path = [beginWord]
        self._dfs(beginWord, endWord, successors, path, res)
        return res

    def _bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)
        cur_visited = set()

        found = False

        while queue:
            # 当前层全部可遍历结点
            for _ in range(len(queue)):
                current_word = queue.popleft()
                # 计算与当前结点连接的结点（所有可能的单char替换方式，看在不在set中）这样比 比较set中每一个与当前的diff更快
                word_list = list(current_word)
                for j in range(len(word_list)):
                    origin_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        # 找到连接的节点了
                        if next_word in word_set and next_word not in visited:
                            if next_word == endWord:
                                found = True
                            cur_visited.add(next_word)
                            queue.append(next_word)
                            successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            visited = visited.union(cur_visited)
            cur_visited.clear()
        return found

    def _dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self._dfs(next_word, endWord, successors, path, res)
            path.pop()


# 解法二：
# 我写的，递归找到所有可能的路径，然后取最短的，超时了，因为会遍历的可能性
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        res = []

        def fun(beginWord, endWord, wordList, path, visited):
            if beginWord == endWord:
                res.append(path + [endWord])
                return

            valid = []
            _word = list(beginWord)
            for j in range(len(_word)):
                origin_char = _word[j]
                for k in string.ascii_lowercase:
                    _word[j] = k
                    next_word = ''.join(_word)
                    if next_word in wordList and next_word not in visited and next_word != beginWord:
                        valid.append(next_word)
                _word[j] = origin_char
            if len(valid) == 0:
                return

            for candi in valid:
                visited.append(beginWord)
                fun(candi, endWord, wordList, path + [beginWord], visited)
                visited.pop()
            return

        fun(beginWord, endWord, set(wordList), [], [])

        if len(res) == 0 or res[0] == []:
            return []
        min_len = min(len(path) for path in res)
        return [path for path in res if len(path) == min_len]


if __name__ == "__main__":
    s = Solution()
    print(s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

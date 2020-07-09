class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie = {}
        for word in dictionary:
            t = trie
            for c in word: t = t.setdefault(c, {})
            t['len'] = len(word)
        ls = len(sentence)
        dp = [0] * (ls + 1)
        for i in range(ls - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            t = trie
            for j in range(i, ls):
                if sentence[j] not in t: break
                t = t[sentence[j]]
                if 'len' not in t: continue
                dp[i] = min(dp[i], dp[j + 1])
                if dp[i] == 0: break
        return dp[0]

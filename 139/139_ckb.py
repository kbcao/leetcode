# dp 还是挺容易想到的，看前 （dict中单词的最大长度） 个dp值是否有True的，并且从那个位置到当前位置的串在dict中

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict: return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        max_word_len = max(len(i) for i in wordDict)
        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i - 1, max(-1, i-max_word_len-1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak('leetcode', ['leet', 'code']))

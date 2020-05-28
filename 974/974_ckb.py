# 想到的两种方法都TLE了，思想都是每次以i结尾的时候，看头在哪里，但每次都保存一个从1-i，2-i，3-i的和的列表，
# 于是只需要把当前元素和列表里的元素相加，再去判断%K，O(n^2)的,过不了

# 这题应该是用前缀和来解决的，就是把子数组问题转换成 sum(j)-sum(i) , 这样的话sum函数可以跟着遍历一直累加
# j为当前指针，判断 sum(j)%k -sum(i)%k == 0 里面符合条件的i的个数，即有多少头可以满足到j是valid的
# 因此这里需要保存一个dict，用来记录 sum(i)%k 的值 到 出现的次数 的映射，这样就能o1时间判断到底有几个valid的头啦

class Solution:
    def subarraysDivByK(self, A, K):
        _sums = dict()
        tmp = []
        for num in A:
            tmp2 = []
            for _sum in tmp:
                _sums[_sum + num] = _sums.get(_sum + num, 0) + 1
                tmp2.append(_sum + num)
            _sums[num] = _sums.get(num, 0) + 1
            tmp2.append(num)
            tmp = tmp2
        res = 0
        for _sum in _sums.keys():
            if _sum % K == 0:
                res += _sums[_sum]
        return res


class Solution:
    def subarraysDivByK(self, A, K):
        dp = [0] * len(A)
        dp[0] = 1 if A[0] % K == 0 else 0
        tmp = [A[0]]
        for i in range(1, len(A)):
            increment = 0
            for item in tmp:
                if (item + A[i]) % K == 0:
                    increment += 1
            if A[i] % K == 0:
                increment += 1
            dp[i] = dp[i - 1] + increment
            tmp2 = []
            for _sum in tmp:
                tmp2.append(_sum + A[i])
            tmp2.append(A[i])
            tmp = tmp2
        return dp[-1]


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # 计算累计和
        asum = 0
        # 计算以i为结束的时候累加可能的结果数
        res = 0
        # 由于每次以i为结束的时候都要往回看头在哪，因此用这个dict来记录之前所有可能的开始中前缀和为特定值的个数（因为我们要根据前缀和来判断这个头是否valid）
        # 因为是 sum(j)%k -sum(i)%k == 0，因此是截取的[i+1,k]的数组，因此要初始化 sum(0)%k 有一个
        sum_x_mod_k_value_2_cnt = {0: 1}
        for num in A:
            # 累加
            asum += num
            asum_mod_k = asum % K
            # 拿到所有valid的开头的数量，即 sum(i)%k == sum(j)%k 
            history_cnt = sum_x_mod_k_value_2_cnt.get(asum_mod_k, 0)
            # 对于当前尾巴来说，这些valid的开头的数量就是当前尾巴的所有可能结果了
            res += history_cnt
            # 把当前值放入dict
            sum_x_mod_k_value_2_cnt[asum_mod_k] = history_cnt + 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

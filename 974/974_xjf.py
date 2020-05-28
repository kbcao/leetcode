class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        h = {0: 1}
        sum = 0
        res = 0
        for a in A:
            sum += a
            key = sum % K
            if key < 0: key += K
            if key not in h: h[key] = 0
            res += h[key]
            h[key] += 1
        return res
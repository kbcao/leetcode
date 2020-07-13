class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for n in nums1:
            dic.setdefault(n, 0)
            dic[n] += 1
        res = []
        for n in nums2:
            if dic.get(n, 0) > 0:
                res.append(n)
                dic[n] -= 1
        return res
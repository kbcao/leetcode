class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic, res = {}, []
        for n in nums:
            dic.setdefault(n, 0)
            dic[n] += 1
        nums = list(dic.keys())
        nums.sort()
        for i in range(len(nums)):
            n1 = nums[i]
            if n1 > 0: break
            if dic[n1] > (2 if n1 == 0 else 1) and n1 * -2 in dic:
                res.append([n1, n1, n1 * -2])
            for j in range(i + 1, len(nums)):
                n2, n3 = nums[j], -n1 - nums[j]
                if n3 < n2: break
                if n3 in dic and (dic[n3] > 1 or n2 != n3):
                    res.append([n1, n2, n3])
        return res
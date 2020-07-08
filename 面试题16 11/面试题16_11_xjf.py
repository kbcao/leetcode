class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0: return []
        res = [shorter * k]
        diff = longer - shorter
        if diff == 0: return res
        for i in range(k): res.append(res[-1] + diff)
        return res

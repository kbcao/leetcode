class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        lv, lp = len(value), len(pattern)
        if lp == 0: return lv == 0
        na, nb = 0, 0
        for c in pattern:
            if c == 'a': na += 1
            else: nb += 1
        for la in range(1 if na == 0 else lv // na + 1):
            lb = 233 if nb == 0 else (lv - la * na) // nb
            if la * na + lb * nb != lv: continue
            a, b = None, None
            idx = 0
            success = True
            for p in pattern:
                if p == 'a':
                    if a == None:
                        a = value[idx:idx + la]
                        if a == b: success = False
                    elif value[idx:idx + la] != a:
                        success = False
                    idx += la
                else:
                    if b == None:
                        b = value[idx:idx + lb]
                        if a == b: success = False
                    elif value[idx:idx + lb] != b:
                        success = False
                    idx += lb
                if not success: break
            if success:
                print(a, b)
                return True
        return False

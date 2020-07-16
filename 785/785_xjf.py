class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        part = [0] * len(graph)
        import queue
        q = queue.Queue()
        for i in range(len(graph)):
            if part[i] != 0: continue
            part[i] = 1
            q.put(i)
            while not q.empty():
                cur = q.get()
                for e in graph[cur]:
                    if part[e] == 0:
                        part[e] = -part[cur]
                        q.put(e)
                    elif part[e] == part[cur]: return False
        return True

class CQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def appendTail(self, value: int) -> None:
        self.st2.append(value)

    def deleteHead(self) -> int:
        if len(self.st1) == 0:
            while len(self.st2) > 0:
                self.st1.append(self.st2.pop())
        try: return self.st1.pop()
        except: return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
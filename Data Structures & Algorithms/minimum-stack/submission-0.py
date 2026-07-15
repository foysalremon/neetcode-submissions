class MinStack:

    def __init__(self):
        self.container = deque()
        self.minS = deque()

    def push(self, val: int) -> None:
        if not self.container:
            self.minS.append(val)
        else:
            self.minS.append(min(val, self.getMin()))
        self.container.append(val)
        
    def pop(self) -> None:
        self.container.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.minS[-1]
        

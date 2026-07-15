class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        valStack = deque()
        iStack = deque()

        for i in range(0, length):
            if not valStack or temperatures[i] <= valStack[-1] :
                valStack.append(temperatures[i])
                iStack.append(i)
            else:
                while valStack and temperatures[i] > valStack[-1]:
                    index = iStack.pop()
                    valStack.pop()
                    res[index] = i - index
                valStack.append(temperatures[i])
                iStack.append(i)

        return res
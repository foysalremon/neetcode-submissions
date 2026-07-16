class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ii, height = stack.pop()
                res = max(res, height * (i - ii))
                start = ii
            stack.append([start, h])

        if stack:
            length = len(heights)
            for i, h in stack:
                res = max(res, h * (length - i))

        return res
        

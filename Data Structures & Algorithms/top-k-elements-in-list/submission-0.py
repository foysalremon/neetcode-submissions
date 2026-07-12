class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        max_count = len(nums)
        buckets = [[] for _ in range(max_count + 1)]

        for val, cnt in freq.items():
            buckets[cnt].append(val)

        res = []
        for cnt in range(len(buckets) - 1, 0, -1):
            for val in buckets[cnt]:
                res.append(val)
                if len(res) == k:
                    return res
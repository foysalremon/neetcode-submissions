class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)

        fleet = 0
        time = 0
        for p, s in pairs:
            cur_time = (target - p)/s

            if cur_time > time:
                fleet += 1
                time = cur_time

        return fleet
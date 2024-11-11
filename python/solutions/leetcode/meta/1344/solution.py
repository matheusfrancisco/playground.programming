# 1344. Angle Between Hands of a Clock
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_d = minutes * (360/60)
        hour_d = (hour * 360/12) + (360/12 * minutes/60)

        diff = abs(min_d - hour_d)
        return min(diff, 360 - diff)

print(Solution().angleClock(12, 30))  # 165.0

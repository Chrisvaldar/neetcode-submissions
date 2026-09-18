from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.name = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.name[key]
        left = 0
        right = len(times) - 1
        best = ""

        while left <= right:
            mid = (left + right) // 2 

            time, val = times[mid]

            if time == timestamp:
                return val
            elif time < timestamp:
                left = mid + 1
                best = val
            else:
                right = mid - 1
        return best

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.record = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        currList = self.record[key]
        left = 0
        right = len(currList) - 1
        best = None

        while left <= right:
            mid = (left + right) // 2
            midTime, midVal = currList[mid]
            
            if midTime == timestamp:
                return midVal
            elif midTime < timestamp:
                best = midVal
                left = mid + 1
            else:
                right = mid - 1
        return best if best is not None else ""

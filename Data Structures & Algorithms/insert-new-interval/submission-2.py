class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False

        for curr in intervals:
            if curr[1] >= newInterval[0] and curr[0] <= newInterval[1] and not inserted:
                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]
            elif not inserted and curr[1] < newInterval[0]:
                res.append(curr)
            else:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(curr)
            print(res)
            print(newInterval)

        if not inserted:
            res.append(newInterval)

        return res
                
            
            
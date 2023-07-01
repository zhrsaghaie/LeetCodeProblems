class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        if len(intervals) == 0 or (len(intervals) > 0 and newInterval[0] > intervals[-1][0]):
            intervals.append(newInterval)

        print(intervals)
        n = len(intervals)
        i = 0
        while i < n - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                # mergethem
                # print("merge", intervals[i], intervals[i+1])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                del intervals[i + 1]
                n -= 1
                i -= 1
            i += 1

        return intervals
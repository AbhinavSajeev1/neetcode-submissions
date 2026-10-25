class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]] 

        for start, end in intervals[1:]:
            lastVal = output[-1][1]

            if start <= lastVal:
                output[-1][1] = max(end, lastVal)
            else:
                output.append([start, end])
        return output 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]] 

        for start, end in intervals[1:]:
            lastEndVal = res[-1][1]
            if lastEndVal >= start: 
                res[-1][1] = max(lastEndVal, end)
            else:
                res.append([start, end])
        return res
            
            
            
        
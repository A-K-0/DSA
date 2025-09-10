class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        new = []

        i = 0
        n = len(intervals)
        
        
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+= 1

        while i < n and intervals[i][0] <= newInterval[1]:
            
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1

        res.append(newInterval)


        while i < n:
            res.append(intervals[i])
            i += 1

        return res


            
        

        for interval in intervals:
            if interval[1] > newInterval[0]:
                new.append(newInterval[0])

            else:
                res.append(interval)

            if interval[0] < newInterval[1]:
                new.append(newInterval[0])

            else:
                res.append(interval)

            

            if interval[0]> newInterval[1]:
                res.append(interval)

            



        
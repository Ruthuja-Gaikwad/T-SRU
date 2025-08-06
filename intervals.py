class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev=float("-inf")
        count=0
        for i in intervals:
            start,end=i
            if start<prev:
                count+=1
            else:
                prev=end
        return count


        

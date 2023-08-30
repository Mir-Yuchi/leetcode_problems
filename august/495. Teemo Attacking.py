class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries == []:
            return 0
        if len(timeSeries) == 1:
            return duration
        count = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                count += duration
            else:
                count += timeSeries[i+1] - timeSeries[i]
        return count + duration
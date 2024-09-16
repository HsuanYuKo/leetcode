class Solution(object):
    def diff(self, s_t1, s_t2):
        t1_h = int(s_t1.split(":")[0])
        t1_m = int(s_t1.split(":")[1])
        t2_h = int(s_t2.split(":")[0])
        t2_m = int(s_t2.split(":")[1])
        minute1 = abs(((t1_h * 60) + t1_m) - ((t2_h * 60) + t2_m))
        minute2 = 24*60 - abs(((t1_h * 60) + t1_m) - ((t2_h * 60) + t2_m))
        return min(minute1, minute2)


    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        min_minutes = 60 * 24
        uniq_timePoints = list(set(timePoints))
        if len(uniq_timePoints) != len(timePoints):
            return 0
        for i in range(0, len(uniq_timePoints)-1):
            for j in range(i+1, len(uniq_timePoints)):
                minutes = self.diff(uniq_timePoints[i], uniq_timePoints[j])
                if minutes < min_minutes:
                    min_minutes = minutes

        return min_minutes
        

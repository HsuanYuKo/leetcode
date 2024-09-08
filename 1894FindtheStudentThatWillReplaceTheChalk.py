class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        chalk_sum = sum(chalk)
        k = k % chalk_sum
        for i in range(0, len(chalk)):
            k = k - chalk[i]
            if k < 0:
                return i

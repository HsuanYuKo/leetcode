class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        count = 0
        max_count = 0
        for i in nums:
            if i == m:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
        return max_count

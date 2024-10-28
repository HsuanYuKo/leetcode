class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        Max_count = 0
        for i in nums:
            count = 0
            tmp = i
            while tmp*tmp in nums:
                count += 1
                tmp = tmp*tmp
            if count > Max_count:
                Max_count = count
        if Max_count == 0:
            return -1
        else:
            return Max_count + 1

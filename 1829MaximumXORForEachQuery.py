class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [0]*len(nums)
        n = (2**maximumBit) - 1
        for i in range(0, len(nums)):
            n = n ^ nums[i]
            ans[i] = n
        return ans[::-1]

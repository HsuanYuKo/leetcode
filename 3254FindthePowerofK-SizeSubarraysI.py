class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(0, len(nums) - k + 1):
            check = True
            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    check = False
                    break
            if check:
                ans.append(nums[i + k - 1])
            else:
                ans.append(-1)
        return ans

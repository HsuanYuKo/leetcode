class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""
        ans_list = []
        
        if sum(nums) == 0:
            return "0"

        ans_list.append(nums[0])

        for i in range(1, len(nums)):
            for j in range (0, len(ans_list)):
                if  int(str(nums[i]) + str(ans_list[j])) >= int(str(ans_list[j]) + str(nums[i])):
                    ans_list.insert(j, nums[i])
                    break
                elif j == len(ans_list) -1 :
                    ans_list.append(nums[i])

        for i in ans_list:
            ans += str(i)
        
        return ans        

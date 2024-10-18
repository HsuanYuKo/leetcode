class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Max = 0
        for i in nums:
            Max = Max | i

        arr = []
        
        for i in nums:
            for j in range(0, len(arr)):
                arr.append(arr[j][:])
                arr[j].append(i)
            arr.append([i])
            # print(arr)

        count = 0
        for i in arr:
            n = 0
            for x in i:
                n = n | x
            if n == Max:
                count += 1

        
        return count


        # for i in nums:
        #     for j in range(0, len(arr)):
        #         arr.append(arr[j])
        #         arr[j] = arr[j] | i
        #     arr.append(i)

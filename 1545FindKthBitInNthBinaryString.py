class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        num = "0"
        for i in range(0, n - 1):
            pre = num
            num = pre + "1"
            suff = pre[::-1]
            new_suff = ""
            for j in suff:
                if j == "0":
                    new_suff += "1"
                else:
                    new_suff += "0"
            num = num + new_suff

            #print(num)
        
        return num[k - 1]

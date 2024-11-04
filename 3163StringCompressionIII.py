class Solution:
    def compressedString(self, word: str) -> str:
        w = [char for char in word]
        pre = w[0]
        count = 0
        ans = ""
        for i in w:
            if i != pre or count > 8:
                ans = ans + str(count)
                ans = ans + pre
                pre = i
                count = 0
            count += 1
        
        if count > 0:
            ans = ans + str(count)
            ans = ans + pre

        return ans

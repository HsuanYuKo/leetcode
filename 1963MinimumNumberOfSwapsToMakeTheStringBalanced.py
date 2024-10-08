class Solution:
    def minSwaps(self, s: str) -> int:
        arr = []
        for i in s:
            if len(arr) > 0:
                if i == "]" and arr[-1] == "[":
                    arr.pop(-1)
                else:
                    arr.append(i)
            else:
                arr.append(i)
            
        if len(arr) == 0:
            return 0
        else:
            return ((len(arr) // 2) + 1) // 2

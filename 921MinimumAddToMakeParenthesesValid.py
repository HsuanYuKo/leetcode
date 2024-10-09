class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []
        for i in s:
            if len(arr) != 0:
                if arr[-1] == "(" and i == ")":
                    arr.pop(-1)
                else:
                    arr.append(i)
            else:
                arr.append(i)
        return len(arr)

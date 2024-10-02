class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = sorted(set(arr))
        arr_dict = {}
        for i, j in enumerate(arr_set, start = 1):
            arr_dict[j] = i
        
        for i in range(0, len(arr)):
            arr[i] = arr_dict[arr[i]]

        return arr

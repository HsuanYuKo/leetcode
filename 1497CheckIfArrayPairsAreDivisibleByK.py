class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        record = {}
        for i in range(0, k):
            record[i] = 0

        for i in range(0, len(arr)):
            record[arr[i]%k] += 1



        if record[0] % 2 != 0:
            return False
        
        check_time = 0
        if len(record)/2 == 0:
            check_time = len(record)//2
        else:
            check_time = len(record)//2 + 1

        for i in range (1, check_time):
            if record[i] != record[k - i]:
                return False
        return True

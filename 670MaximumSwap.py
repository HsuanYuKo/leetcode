class Solution:
    def maximumSwap(self, num: int) -> int:
        n = [ x for x in str(num)]
        max_value = num
        for i in range(0, len(n) - 1):
            for j in range(i + 1, len(n)):
                n[i], n[j] = n[j], n[i]
                tmp = "".join(n)
                if int(tmp) > int(max_value):
                    max_value = tmp
                n[i], n[j] = n[j], n[i]
        return int(max_value)

class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        count = 0
        black = 0

        for i in range(0, len(s)):
            if s[i] == '1':
                black += 1
            else:
                count += black
                
        return count
                

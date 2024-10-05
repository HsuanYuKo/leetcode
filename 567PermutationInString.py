class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set_s1 = {}
        for i in s1:
            if i in set_s1:
                set_s1[i] += 1
            else:
                set_s1[i] = 1

        for i in range(0, len(s2) - len(s1) + 1):
            set_s2 = {}
            for j in range(i, i + len(s1)):
                if s2[j] in set_s2:
                    set_s2[s2[j]] += 1
                else:
                    set_s2[s2[j]] = 1
            if set_s1 == set_s2:
                return True

        return False

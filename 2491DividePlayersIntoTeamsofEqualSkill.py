class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        ans = []
        Sum = skill[0] + skill[-1]
        for i in range(0, len(skill) // 2):
            tmp = skill[i] + skill[len(skill) - i - 1]
            if tmp != Sum:
                return -1
            else:
                tmpans = [skill[i], skill[len(skill) - i - 1]]
                ans.append(tmpans) 

        ans_sum = 0
        for i, j in ans:
            ans_sum += i * j

        return ans_sum

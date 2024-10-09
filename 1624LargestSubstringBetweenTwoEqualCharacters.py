class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_dict = {}
        char = []
        for i in s:
            if s.count(i) > 1 and i not in char:
                char.append(i)

        if len(char) == 0:
            return -1

        for i in char:
            first = s.find(i)
            last = s.rfind(i)
            char_dict[i] = last- first - 1
        
        return max(char_dict.values())

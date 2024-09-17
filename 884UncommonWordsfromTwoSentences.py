class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2
        w = s.split(" ")

        w.sort()
        repeat = []
        for i in range(0, len(w) - 1):
            # print w, repeat
            # print w[i], w[i+1], i
            if w[i] == w[i + 1]:
                if w[i] not in repeat:
                    repeat.append(w[i])
        
        ans = []
        for i in range(0, len(w)): 
            #print (i, list(set(repeat)))
            if w[i] not in repeat:
                ans.append(w[i])
        return ans

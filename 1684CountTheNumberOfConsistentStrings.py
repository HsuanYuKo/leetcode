class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
        allow = list(allowed)
        ans = len(words)
        if len(allowed) == 26:
            return ans
            
        for i in words:
            # word = [x for x in i]
            word = set(list(i))
            flag = False
            for j in word:
                for k in allow:
                    if j == k:
                        flag = True
                        break
                    else:
                        flag = False

                if not flag:
                    ans -= 1
                    break
        return ans
            
                

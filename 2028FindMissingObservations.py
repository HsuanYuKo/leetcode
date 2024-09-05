class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        sum_roll=len(rolls)+n
        lack=(mean*sum_roll)-sum(rolls)
        if lack > n*6 or lack<0:
            return []
        else:
            ans=[lack/n for i in range(0,n)]
            if lack%n!=0:
                print lack%n
                for i in range(0, lack%n):
                    ans[i]+=1
            if 0 in ans:
                return []
            return ans

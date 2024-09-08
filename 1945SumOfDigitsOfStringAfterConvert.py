class Solution(object):
    def repeat(self,ans,k):
        ans=str(ans)
        k2=0
        for i in range(0,len(ans)):
            k2=k2+int(ans[i])
        return k2

    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(0, len(s)):
            n=ord(s[i])-96
            if n<10:
                ans=ans+n
            else:
                ans=ans+n/10
                ans=ans+n%10
        
        for i in range(0,k):
            print i
            if (i+1)==k or ans<10:
                return ans
            ans=self.repeat(ans,k)

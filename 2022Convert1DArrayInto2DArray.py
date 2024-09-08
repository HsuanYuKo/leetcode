class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m*n:
            return []
        ans = [[0 for i in range(0, n)]for i in range(0, m)]
        x = 0
        for i in range(0, m):
            for j in range(0, n):
                ans[i][j] = original[x]
                x += 1
        return (ans)

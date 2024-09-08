class Solution(object):

    def dfs(self, grid2, i, j, island):
        m = len(grid2[0])
        n = len(grid2)
        if (i < 0 or j < 0 or j >= len(grid2[0]) or i >= len(grid2)):
            return
        

        if(grid2[i][j] == 0):
            return
        
        grid2[i][j] = 0
        island.append((i, j))
        self.dfs(grid2, i, j - 1, island) #上
        self.dfs(grid2, i, j + 1, island) #下
        self.dfs(grid2, i - 1, j, island) #左
        self.dfs(grid2, i + 1, j, island) #右


    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """


        grid2_count = 0
        grid2_island_set = []
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if(grid2[i][j] == 1):
                    grid2_count += 1
                    island = []
                    self.dfs(grid2, i, j, island)
                    grid2_island_set.append(island)

        

        count = 0
        for i in range(len(grid2_island_set)):
            check = True
            for j in range(len(grid2_island_set[i])):
                if grid1[grid2_island_set[i][j][0]][grid2_island_set[i][j][1]] == 0:
                    check = False
            if check:
                count += 1

        return(count)

class Solution :

    def numIslands(self, grid) :

        if len(grid) == 0 :

            return 0

        num_of_islands = 0

        for i in range(len(grid)) :

            for j in range(len(grid[0])):

                if grid[i][j] == '1' :

                    num_of_islands += self.island_counter(grid, i, j) 

        return num_of_islands

    
    def island_counter(self, grid, i, j) :

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' :

            return 0

        grid[i][j] = '0'

        self.island_counter(grid, i + 1, j)

        self.island_counter(grid, i - 1, j)

        self.island_counter(grid, i, j + 1)

        self.island_counter(grid, i, j - 1)

        return 1


s = Solution()

print(s.numIslands([['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]))
```python3

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j>0 and i>0:
                    grid[i][j]+=min(grid[i][j-1],grid[i-1][j])
                elif j>0:
                    grid[i][j]+=grid[i][j-1]
                elif i>0:
                    grid[i][j]+=grid[i-1][j]
        return grid[-1][-1]

```

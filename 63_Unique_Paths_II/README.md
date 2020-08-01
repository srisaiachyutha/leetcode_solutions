```python3

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # with out changing the given obstacleGrid 
        
        # if the first cell is a obstacle we cannot go another cell at all
        # so directly returning zero
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        
        
        # making the dp[j] = 1 when there is no obstacle
        # once we reach a obstacle we cannot go to the another cell
        # in the first row so we make every other elements to 0 directly
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp.append(abs(obstacleGrid[0][j]-1))
                continue
            for i in range(j,n):
                dp.append(0)
            break
        
        # we have to do the same thing as itertating the first row for the
        # first column but we can directly do it in the iteration itself
        # of the matrix
        for i in range(1,m):
            # here we are making the cell to 0 because after we have seen 
            # an obstacle in the first column we cannot go to next cell
            # in the first column so making it zero here
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            
            for j in range(1,n):
                # if no obstacle present in the present cell of iteration
                # we make to add previous cell value to the present cell
                # which is equal to grid[i][j] = grid[i-1][j] + grid[i][j-1]
                # making it to directly dp[j] = dp[j] + dp[j-1]
                # for reducing the space
                if obstacleGrid[i][j] == 0:
                    dp[j] += dp[j-1]
                else:
                    # if we see the obstacle we can make the present dp[j] = 0
                    dp[j] = 0  
        # last cell contains the solution returning it
        return dp[-1]

```

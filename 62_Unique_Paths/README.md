### O(n^2) time and O(n^2) space approach 

```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
```

### O(n^2) time and O(n) space approach

```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]
```

### O(n) time and O(1) space approach

```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial as f
        return int(f(m+n-2)/f(m-1)/f(n-1))
```

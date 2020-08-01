##Using the Kadens algorithm 

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localmax =nums[0]
        globalmax=nums[0]
        for i in nums[1::]:
            localmax = max(localmax+i ,i)
            globalmax = max(globalmax,localmax)
        return globalmax
```

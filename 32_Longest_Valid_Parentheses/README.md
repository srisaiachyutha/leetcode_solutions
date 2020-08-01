making the string whether valid or not by making 1's in those positions 
```
making the string whether valid or not by making 1's in those positions 

input  :   )    (    )    (     )    )
dp     :   0    0    0    0     0    0
after  :   0    1    1    1     1    0
after iterrating it will become  like this and we make the longest continuous ones sum as our ans for it .

```
after iterrating it will become  like this and we make the longest continuous ones sum as our ans for it .

```python3
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # making the valid or not in the dp table 
        count = 0
        stack = []
        dp = [0]*len(s)
        for j,i in enumerate(s):
            # when ever we see '(' we will put it into the stack
            if i=='(':
                stack.append(j)
            else:
                # when ever we see ')' we will pop the index in stack
                # and make that index as good which means 1 here
                # and also the present index position also good
                # we are matching the ending paranthesis with 
                # starting paranthesis indices 
                if stack:
                    dp[j]=1
                    dp[stack.pop()]=1
        m = 0
        # we are taking the longest consicutive one's length 
        # which means it is our ans for longest valid parentheses 
        # substring
        for i in dp:
            if i==1:
                count+=1
            else:
                m = max(m,count)
                count=0
        m = max(m,count)
        return m
```




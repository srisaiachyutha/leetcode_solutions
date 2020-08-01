```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength = 0
        left,right = 0,0
        l = len(s)
        for i in range(len(s)):
            c = 1
            count=1
            # making the present element as center and exploring 
            # both sides and increasing the count and remembering
            # the start and end position of the string
            while i-c>=0 and i+c<l:
                if s[i-c]==s[i+c]:
                    count+=2
                else:
                    break
                c+=1
            if count>maxlength:
                maxlength = count
                left,right = i-c+1,i+c-1
            # making the present element as not center and exploring
            # both sides of string
            c = 0
            count = 0
            while i-c>=0 and i+c+1<l:
                if s[i-c]==s[i+c+1]:
                    count+=2
                else:
                    break
                c+=1
            if count>maxlength:
                maxlength = count
                left,right = i-c+1,i+c+1-1
        return s[left:right+1]
```

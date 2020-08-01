class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n<0:
            n = abs(n)
            flag = True
        else:
            flag = False
        while n>0:
            #high speed pow calculation is done here
            if n%2 == 1:
                result*=x
            #here we will increase the value doble of it which will reduce the time complexity
            x*=x
            n//=2
        if flag:
            return 1/result
        return result
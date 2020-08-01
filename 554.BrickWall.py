class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if sum(wall[0])==1:
            return len(wall)
        d ={}
        for i in wall:
            s =0
            for j in range(len(i)-1):
                s+=i[j]#here we are calculating the cuts where they will happen 
                d[s] = d.get(s,0)+1
        #print(d)
        if len(d.values())>0:
            #here we will calculate the through how many the line will pass through bricks
            return len(wall)-max(d.values())
        return len(wall)